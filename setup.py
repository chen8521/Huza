# coding=utf-8
# !/usr/bin/env python
# python 3.6.5
# author: hufei
import codecs
import os
import re

# 1. python setup.py bdist_wheel
# 2. wheel convert huza-0.1.2-py36.egg
# 3. twine upload huza-0.1.2-py36-none-any.whl

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


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.rst'), 'r', 'utf-8') as handle:
    readme = handle.read()

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
    long_description=readme,
    url='https://github.com/huyidao625/Huza',
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
        'Environment :: X11 Applications :: Qt',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries'
    ],
    project_urls={
        'Wiki': 'https://www.hudh.cn'
    }

)
