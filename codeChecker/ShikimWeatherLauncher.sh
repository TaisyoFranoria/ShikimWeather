#!/bin/bash

export SCRIPT_DIR="$(cd $(dirname $0); pwd)"
export WORK_DIR="${SCRIPT_DIR}/work"
export DAYRY_DATAFILE=$(date "+%Y%m%d")


if [ ! -e ${WORK_DIR}/${DAYRY_DATAFILE} ];then
    echo "今日の天気を調べるね"
    if [ -n ${1} ];then
       python3 ${SCRIPT_DIR}/Outputer.py ${1} > ${WORK_DIR}/${DAYRY_DATAFILE}
    else 
       python3 ${SCRIPT_DIR}/Outputer.py "130000" > ${WORK_DIR}/${DAYRY_DATAFILE}
    fi
    
    if [ $? -ne 0 ];then
       rm -f ${WORK_DIR}/${DAYRY_DATAFILE}
    fi
fi

${SCRIPT_DIR}/../ShikimiShellArt.sh 0 $(cat ${WORK_DIR}/${DAYRY_DATAFILE})


