#!/bin/bash

ROOT_PATH=/config/workspace/project
CONFIG_PATH=$ROOT_PATH/utils/configs.json

int_port=$(cat ${CONFIG_PATH} | jq '.int_web_port')
check=`ps -ef | grep ${int_port} | wc | awk '{print $1}'`

if [ $check -gt 1 ]; then
    echo '현재 웹 서버가 실행중입니다.'

else

    LOG_PATH=${ROOT_PATH}/MC-Worlds/src/logs/web

    echo "실행코드가 있는 곳으로 이동 \n"
    cd ${ROOT_PATH}/MC-Worlds/src/web
    echo "현재 작업 디렉토리 입니다."
    pwd

    today=$(date "+%Y-%m-%d")
    yesterday=$(date -d "yesterday" "+%Y-%m-%d")

## 어제 날짜의 로그 파일 압축
    mkdir $LOG_PATH/${yesterday}_logs
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
        mkdir $LOG_PATH
        echo "로그를 저장할 폴더가 생성되었습니다."
        idx='000'
    fi

    ## shell script가 실행 될 때의 로그 파일 경로
    LOG_PATH=${LOG_PATH}/${today}_web_${idx}.log
    echo 이번에 생성할 로그 파일 경로 입니다. ${LOG_PATH}

    ## 백그라운드에서 API 서버를 실행시키고, 로그는 로그 파일 디렉토리에 저장
    echo "\nAPI 서버를 실행합니다."
    echo "\nssl 서버로 웹 서버를 실행합니다."
    # nohup python manage.py runsslserver \
    #      --certificate "/config/workspace/project/utils/keys/fullchain1.pem" \
    #      --key "/config/workspace/project/utils/keys/privkey1.pem" \
    #      0:${int_port} > $LOG_PATH &

    nohup python manage.py runserver 0:${int_port} > $LOG_PATH &
fi