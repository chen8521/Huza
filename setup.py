# coding=utf-8
# !/usr/bin/env python
# python 3.6.5
# author: hufei
import os
import re

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

version = re.compile(r'VERSION\s*=\s*\'(.*?)\'')


def get_package_version():
    "returns package version without importing it"
    base = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(base, "huza/util/version.py")) as initf:
        for line in initf:
            m = version.match(line.strip())
            if not m:
                continue
            return m.groups()[0]


version = get_package_version()


def get_requirements():
    file_data = open('requirements.txt').read().splitlines()
    return file_data


setup(
    name="huza",
    version=version,
    author='hufei',
    author_email='hufei625@qq.com',
    packages=find_packages(include=['huza', 'huza.*']),
    description="Self-use pyqt framework",
    license="MIT License",
    install_requires=get_requirements(),
    zip_safe=True,
    data_files=[('nsis', ['nsis.nsi']),
                ],
    entry_points={
        'console_scripts': [
            'huza=huza.cli.shell:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: System :: Networking',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
