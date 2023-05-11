#!/bin/bash

## ROOT_PATH, CONFIG_PATH 설정
ROOT_PATH=/config/workspace/project
CONFIG_PATH=$ROOT_PATH/utils/configs/ports.json

## CONFIG 파일에 저장되어 있는 내부 포트 값을 불러와서
## 현재 실행되고 있는 프로세스에 내부 포트 값이 들어가는 항목이 있는지 확인
int_port=$(cat ${CONFIG_PATH} | jq '.mrcon_api_int_port')
check=`ps -ef | grep player_check | wc | awk '{print $1}'`

## 현재 실행되고 있는 프로세스에 api 내부 포트 값이 들어가는 항목이 있다면 넘어감.
if [ $check -gt 1 ]; then
    echo '현재 프로그램이 실행중입니다.'

## 없다면 이쪽으로 넘어옴.
else

    ## 로그파일을 저장할 경로 지정
    LOG_PATH=${ROOT_PATH}/logs/mcrcon

    ## 코드가 저장되어 있는 working directory로 이동 
    echo "실행코드가 있는 곳으로 이동 \n"
    cd $ROOT_PATH/MC-Worlds/src
    echo "현재 작업 디렉토리 입니다."
    pwd

    ## 오늘 날짜와 어제 날짜 지정
    today=$(date "+%Y-%m-%d")
    yesterday=$(date -d "yesterday" "+%Y-%m-%d")

    ## 어제 날짜의 로그 파일 압축
    mkdir -p $LOG_PATH/${yesterday}_logs
    mv $LOG_PATH/${yesterday}*.* $LOG_PATH/${yesterday}_logs
    zip -r $LOG_PATH/${yesterday}_logs.zip $LOG_PATH/${yesterday}_logs
    rm -rf $LOG_PATH/${yesterday}_logs


    echo "\n오늘 날짜 입니다." $today

    ## 로그 파일을 저장하는 디렉토리가 있는 경우
    if [ -d $LOG_PATH ]; then
        echo "\n로그를 저장할 폴더가 이미 존재합니다."

        ## 로그 파일 디렉토리에 오늘 날짜의 로그 파일 개수를 확인하여 
        ## 이번 로그 파일의 인덱스 값으로 사용      
        ## e.g.) 로그 파일 디렉토리에 3개의 파일이 있음. -> idx = 3
        idx=$(ls -l $LOG_PATH | grep $today | grep ^- | wc -l)

        ## 로그 파일 정렬을 위해 앞에 0을 붙여 인덱스를 3자리 수로 만들어줌.
        ## e.g.) idx = 3 -> idx = 003, idx = 10 -> idx = 010
        while [ ${#idx} -ne 3 ]; do
            idx="0"$idx
        done

    ## 로그 파일을 저장하는 디렉토리가 없는 경우
    else
        ## 로그 파일 디렉토리를 생성하고, 로그 파일의 인덱스 값을 000으로 설정
        mkdir -p $LOG_PATH
        echo "로그를 저장할 폴더가 생성되었습니다."
        idx='000'
    fi

    ## shell script가 실행 될 때의 로그 파일 경로
    LOG_PATH=${LOG_PATH}/${today}_player_${idx}.log
    echo 이번에 생성할 로그 파일 경로 입니다. ${LOG_PATH}

    ## 백그라운드에서 API 서버를 실행시키고, 로그는 로그 파일 디렉토리에 저장
    echo "\nAPI 서버를 실행합니다."
    nohup python player_check.py > $LOG_PATH &

fi