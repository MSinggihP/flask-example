#!/bin/bash
echo -e "\nBase Directory and Filename..."
BASEDIR0="$( cd "$( dirname "$0" )" && pwd )"
CURRDIR0=${BASEDIR0##*/}
FILENAME=`basename $0`; FILE=$(echo $FILENAME | cut -d '.' -f 1) 
echo [$BASEDIR0] [$CURRDIR0] [$FILENAME] [$FILE]
echo "......."
cd $BASEDIR0
pip install -r requirements.txt
export FLASK_APP=app/main.py
export FLASK_ENV=development
flask $FILE
exit 0
