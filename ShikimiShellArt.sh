#!/bin/bash

Mes="メッセージが設定されてないよ"

if [ $# -eq 1 ]; then
    if [ $1 -eq 1 ]; then
        emo=("_" "_" "=" "=" "^")
    else 
        emo=("_" "_" "0" "0" "A")
    fi
elif [ $# -eq 2 ]; then
    if [ $1 -eq 1 ]; then
        emo=("_" "_" "=" "=" "^")
        Mes=$2
    else 
        emo=("_" "_" "0" "0" "A")
        Mes=$2
    fi
else 
    emo=("_" "_" "0" "0" "A")
fi




echo "  __----__"
echo " /           "
echo " |  /${emo[0]}// ${emo[1]}/ |"
echo "|  / ${emo[2]}   ${emo[3]}| \\"
echo "\  \   ${emo[4]}   ) \\"
echo " \  |~|_|~/"
echo "  /   | | \\ "
echo " /  ] | |[ \\"
echo "/     | |   \\"
echo "-------------"
echo "$Mes"

#追加質問
#read -t 5 -p "ほかになんか用ある？(y/n)" ANS
#echo ""
#if [ "$ANS" = "" ]; then
 #      echo "なんか言えよ"
#else
 #      echo "ま、なんかあるわけじゃないんだけどね"
#fi

