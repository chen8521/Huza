import hashlib
import shutil
import subprocess
import sys

from util.version import VERSION

version = VERSION
from frog_ribon import DEBUG

if DEBUG:
    print('\033[91m不能在DEBUG模式下打包\033[0m')
    exit(-1)
shutil.rmtree('build', ignore_errors=True)
shutil.rmtree('dist', ignore_errors=True)

p1 = subprocess.Popen(
    ['pyinstaller', '-i', 'source/img/logo.ico', '--add-data=venv/Lib/site-packages/matplotlib;matplotlib',
     '--add-data=venv/Lib/site-packages/vtkmodules;vtkmodules',
     '--add-data=venv/Lib/site-packages/numpy;numpy',
     '-D',
     '-w',
     '-y',
     'frog_ribon.py'], cwd='.')
p1.wait()
#
p2 = subprocess.Popen(['makensis', f'/DVersion={version}', 'frog_ribon.nsi'], cwd='.', encoding='gbk')
p2.wait()
