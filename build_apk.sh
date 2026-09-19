#!/usr/bin/env bash
set -e

python3 -m pip install --upgrade pip
python3 -m pip install buildozer cython

# On Ubuntu/Debian, install system build dependencies if they are missing:
# sudo apt update
# sudo apt install -y git zip unzip openjdk-17-jdk autoconf libtool pkg-config \
#   zlib1g-dev libncurses5-dev libncursesw5-dev cmake libffi-dev libssl-dev

buildozer android debug

echo "APK output:"
find bin -maxdepth 1 -type f -name '*.apk' -print
