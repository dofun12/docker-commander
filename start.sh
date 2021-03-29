#!/bin/bash
MAIN_DIR=$(pwd)
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
echo $DIR
cd $DIR
pipenv run python main.py >> $DIR/log.txt 2>&1 &
cd $MAIN_DIR
