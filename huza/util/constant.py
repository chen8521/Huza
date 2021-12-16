# coding=utf-8
import re
import sys

LOGFILE = 'huza.log'

LOGGINGCONFIG = {
    "handlers": [
        {"sink": sys.stdout,
         'format': '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: ^8}</level> | <cyan>{name:^20}</cyan>:<cyan>{function:^30}</cyan>:<cyan>{line:^4}</cyan> - <level>{message}</level>',
         'level': 'DEBUG'},

        {"sink": LOGFILE,
         'format': '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: ^8}</level> | <cyan>{name:^20}</cyan>:<cyan>{function:^30}</cyan>:<cyan>{line:^4}</cyan> - <level>{message}</level>',
         'level': 'INFO'},
    ],
}

FLOAT_RE = re.compile('^[+-]?\d+$|^[-+]?\d*\.\d+$|^[+-]?\d+\.\d+[Ee]{1}[+-]?\d+$')
