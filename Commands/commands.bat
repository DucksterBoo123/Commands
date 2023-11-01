@echo off

DIR="$( cd "$( dirname "$0" )" && pwd )"
echo "Script location: ${DIR}"

cd ${DIR}

python commands.py
