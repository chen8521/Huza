# coding=utf-8
import os
from huza.superclass.mainwindow_run import MainWindowRun


class Extra:
    debug = None
    speed = None

    def __init__(self, debug=False, speed=1):
        self.debug = debug
        self.speed = speed


DEBUG = True
speed = 1000

if 'DEBUG_MODE' in os.environ:
    DEBUG = True
    speed = 100

if __name__ == '__main__':
    extra = Extra(debug=DEBUG, speed=speed)

    app = MainWindowRun(extra)
    app.run()
