# coding=utf-8
import codecs
import datetime
import sys, logging, os, shutil, tempfile
from collections import namedtuple
from tkinter import Tk, messagebox

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from loguru import logger

from huza.mainwindow import MainWindow_Form
from huza.ribbon.qss.default_qss import default_style
from huza.splash import SplashScreen
from huza.util.version import VERSION


class Extra:
    debug = None
    speed = None

    def __init__(self, debug=False, speed=1):
        self.debug = debug
        self.speed = speed

LOGFILE = 'test.log'
try:
    if os.path.exists(LOGFILE):
        os.remove(LOGFILE)
    LOGGINGCONFIG = {
        "handlers": [
            {"sink": sys.stdout,
             'format': '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: ^8}</level> | <cyan>{name:^20}</cyan>:<cyan>{function:^30}</cyan>:<cyan>{line:^4}</cyan> - <level>{message}</level>',
             'level': 'DEBUG'},

            {"sink": codecs.open(LOGFILE, 'w', 'utf-8'),
             'format': '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: ^8}</level> | <cyan>{name:^20}</cyan>:<cyan>{function:^30}</cyan>:<cyan>{line:^4}</cyan> - <level>{message}</level>',
             'level': 'INFO'},

        ],
    }
    logger.configure(**LOGGINGCONFIG)
except Exception:
    root = Tk()
    root.withdraw()
    txt = messagebox.showinfo("程序权限不足", "请右键管理员运行！或者\n右键图标->属性->兼容性->特权等级-勾上管理员运行")
    root.destroy()
    sys.exit(-3)


def except_hook(exc_type, exception, traceback):
    """"""
    msg = ' Traceback (most recent call last):\n'
    while traceback:
        filename = traceback.tb_frame.f_code.co_filename
        name = traceback.tb_frame.f_code.co_name
        lineno = traceback.tb_lineno
        msg += '   File "%.500s", line %d, in %.500s\n' % (filename, lineno, name)
        traceback = traceback.tb_next
    msg += ' %s: %s\n' % (exc_type.__name__, exception)

    logger.exception(exception)
    root = Tk()
    root.withdraw()
    txt = messagebox.showinfo("错误", msg)
    root.destroy()
    sys.__excepthook__(exc_type, exception, traceback)


class MyQmainWindow(QMainWindow):
    def closeEvent(self, QCloseEvent):
        self.closeprocess()
        if not DEBUG:
            r = QMessageBox.question(self, '关闭确认', '是否关闭软件？',
                                     QMessageBox.Yes | QMessageBox.No)
            if r == QMessageBox.Yes:
                return super(MyQmainWindow, self).closeEvent(QCloseEvent)
            else:
                QCloseEvent.ignore()


DEBUG = False
speed = 1000
if 'DEBUG_MODE' in os.environ:
    DEBUG = True
    speed = 100

if __name__ == '__main__':
    import sys

    sys.excepthook = except_hook
    extra = Extra(debug=DEBUG, speed=speed)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    app.setFont(QFont("微软雅黑", 9))
    app.setApplicationName("xxx")
    app.setOrganizationName("Romtek inc")
    app.setOrganizationDomain("Romtek.cn")
    app.setStyleSheet(default_style)
    splash = SplashScreen(":/img/splash.jpg", extra)
    splash.loadProgress()
    mainwindow = MyQmainWindow()
    # mainwindow.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)

    window = MainWindow_Form(extra)
    window.setupUi(mainwindow)
    mainwindow.showMaximized()
    if extra.debug:
        mainwindow.setWindowTitle(f'水下发射高精度数值模拟软件 (Debug) Ver{VERSION}')
    else:
        mainwindow.setWindowTitle(f'水下发射高精度数值模拟软件 Ver{VERSION}')

    mainwindow.setWindowIcon(QIcon(QPixmap(':/img/logo.ico')))
    mainwindow.show()
    splash.finish(mainwindow)
    app.exec_()
