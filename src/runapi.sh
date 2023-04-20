#!/bin/bash

check=`ps -ef | grep 9330 | wc | awk '{print $1}'`
if [ $check -gt 1 ]; then
    echo '현재 API 서버가 실행중입니다.'

else
    echo "실행코드가 있는 곳으로 이동 \n"
    ROOT_PATH=/config/workspace/project/MC-Worlds/src
    LOG_PATH=${ROOT_PATH}/logs/api

    cd $ROOT_PATH
    echo "현재 작업 디렉토리 입니다."
    pwd

    today=$(date "+%Y-%m-%d")
    yesterday=$(date -d "yesterday" "+%Y-%m-%d")


    mkdir $LOG_PATH/${yesterday}_logs
    mv $LOG_PATH/${yesterday}*.* $LOG_PATH/${yesterday}_logs
    zip -r $LOG_PATH/${yesterday}_logs.zip $LOG_PATH/${yesterday}_logs
    rm -rf $LOG_PATH/${yesterday}_logs


    echo "\n오늘 날짜 입니다." $today

    if [ -d $LOG_PATH ]; then
        echo "\n로그를 저장할 폴더가 이미 존재합니다."
        idx=$(ls -l $LOG_PATH | grep $today | grep ^- | wc -l)

        while [ ${#idx} -ne 3 ]; do
            idx="0"$idx
        done

    else
        mkdir $LOG_PATH
        echo "로그를 저장할 폴더가 생성되었습니다."
        idx='000'
    fi

        LOG_PATH=${LOG_PATH}/${today}_api_${idx}.log
        echo 이번에 생성할 로그 파일 경로 입니다. ${LOG_PATH}
        echo "\nAPI 서버를 실행합니다."
        nohup uvicorn api:app --host 0.0.0.0 --port 9330 --reload > $LOG_PATH &

    fi