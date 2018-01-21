#!/usr/bin/env bash
set -e

name=$1
virtualenv3 --python=python3 env
./env/bin/pip install -r requirements

mv botname ${name}
sed "s/botname/${name}/g" main.py