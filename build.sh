#!/bin/bash
cd huza
rm -rf dist
git pull
cd ..
for version in  3.6 3.7 3.8 3.9 3.10 3.11-rc-bullseye
do
    echo "building $version..."
    docker run --rm -v /root/huza/huza:/opt/target python:$version bash -c "pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  --upgrade wheel setuptools pip; cd /opt/target; python setup.py  sdist bdist_egg bdist_wheel"
done
cd huza/dist
twine upload *
