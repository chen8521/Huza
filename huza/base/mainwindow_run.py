import os
import sys
from tkinter import messagebox, Tk

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication
from loguru import logger
from huza.util.constant import LOGGINGCONFIG, LOGFILE
from huza.icons.iconcore import IconListHandler
from huza.mainwindow import MainWindow_Form
from huza.ribbon.qss.default_qss import default_style
from huza.splash import SplashScreen
from huza.base.mainwindow import MyQmainWindow, except_hook

sys.excepthook = except_hook


class MainWindowRun(object):
    def __init__(self, extra):
        self.extra = extra
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        self.app = QApplication(sys.argv)
        self._init_image_list()
        self.app.setFont(QFont("微软雅黑", 9))
        self.app.setApplicationName("")
        self.app.setOrganizationName("")
        self.app.setOrganizationDomain("")
        self.app.setStyleSheet(default_style)
        self.mainwindow = MyQmainWindow()
        self.mainwindow._set_close_waring(extra)
        self.window = MainWindow_Form(extra)
        self.window.setupUi(self.mainwindow)

    def addAction(self, name, text, tip=None, shortcut=None, icon=None, checkable=False, checked=False, slot=None,
                  myactionname=None,
                  enable=True):
        self.window.addAction(name, text, tip, shortcut, icon, checkable, checked, slot, myactionname, enable)

    def _init_log(self):
        try:
            if os.path.exists(LOGFILE):
                os.remove(LOGFILE)
            logger.configure(**LOGGINGCONFIG)
        except Exception as e:
            root = Tk()
            root.withdraw()
            txt = messagebox.showinfo("程序权限不足", f"请右键管理员运行！或者\n右键图标->属性->兼容性->特权等级-勾上管理员运行.\n error: {e}")
            root.destroy()
            sys.exit(-3)

    def _init_image_list(self):
        self.icon_list = IconListHandler()

    def set_style_sheet(self, style: str):
        self.app.setStyleSheet(style)

    def set_splash_pic(self, pic: QPixmap):
        self.splash = SplashScreen(pic, self.extra)
        self.splash.loadProgress()

    def set_window_logo(self, logo: QIcon):
        self.mainwindow.setWindowIcon(logo)

    def set_window_title(self, title: str):
        self.mainwindow.setWindowTitle(title)

    def run(self):
        self.mainwindow.showMaximized()
        self.mainwindow.show()
        if hasattr(self, 'splash'):
            self.splash.finish(self.mainwindow)
        self.app.exec_()
