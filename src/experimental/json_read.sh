#!/bin/bash

ROOT_PATH=/config/workspace/project
JSON_PATH=$ROOT_PATH/utils/configs.json

json=$(cat ${JSON_PATH} | jq '.ext_api_port')
echo $json