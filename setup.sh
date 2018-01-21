#!/usr/bin/env bash
set -e

name=$1
virtualenv3 --python=python3 env
./env/bin/pip install -r requirements.txt

mv botname ${name}
sed -i "s/botname/${name}/g" main.py