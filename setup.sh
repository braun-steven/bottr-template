#!/usr/bin/env bash
set -e

name=$1

mv botname ${name}
sed -i "s/botname/${name}/g" main.py
