import os
import sys
import types
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
        self._init_log()
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        self.app = QApplication(sys.argv)
        self._init_icon_list()
        self.app.setFont(QFont("微软雅黑", 9))
        self.app.setApplicationName("")
        self.app.setOrganizationName("")
        self.app.setOrganizationDomain("")
        self.app.setStyleSheet(default_style)
        self.mainwindow = MyQmainWindow()
        self.mainwindow._set_close_waring(extra)
        self.window = MainWindow_Form(extra, self.icon_list)
        self.window.setupUi(self.mainwindow)

    def addAction(self, name, text, tip=None, shortcut=None, icon=None, checkable=False, checked=False, slot=None,
                  myactionname=None,
                  enable=True):
        self.window.addAction(name, text, tip, shortcut, icon, checkable, checked, slot, myactionname, enable)

    def init_menu(self, rabbons: dict):
        self.window.init_ribbon(rabbons)

    def init_docks(self, docks: dict, layout: list):
        self.window.init_docks(docks, layout)

    def bind_signal(self, signal, func):
        if func.__name__ in dir(self.window):
            raise Exception(f'绑定的函数[{func.__name__}]与内置函数冲突，请更换函数名称')
        setattr(self.window, func.__name__, types.MethodType(func, self.window))
        self.window.bind_signal(signal, getattr(self.window, func.__name__))

    def get_action(self, name: str):
        if name in self.window.actions:
            return self.window.actions.get(name)
        return None

    def get_dock(self, name: str):
        if name in self.window.docks:
            return self.window.docks.get(name)
        return None

    def set_dock_view(self, name, displayname, dockname, formclass):
        self.window.setDockView(name, displayname, dockname, formclass)

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

    def _init_icon_list(self):
        self.icon_list = IconListHandler()

    def add_icon_list(self, name, img_database: dict):
        self.icon_list.add_icon_list(name, img_database)

    def set_style_sheet(self, style: str):
        self.app.setStyleSheet(style)

    def set_splash_pic(self, pic: QPixmap):
        self.splash = SplashScreen(pic, self.extra)
        self.splash.loadProgress()

    def set_window_logo(self, logo: QIcon):
        """设置软件logo"""
        self.mainwindow.setWindowIcon(logo)

    def set_window_title(self, title: str):
        self.mainwindow.setWindowTitle(title)

    def set_init_actions_func(self, func):
        setattr(self, 'init_actions_func', types.MethodType(func, self))

    def set_init_docks_func(self, func):
        setattr(self, 'init_docks_func', types.MethodType(func, self))

    def set_init_connect_func(self, func):
        setattr(self, 'init_connect_func', types.MethodType(func, self))

    def set_init_signal_func(self, func):
        setattr(self, 'init_signal_func', types.MethodType(func, self))

    def set_init_menu_func(self, func):
        setattr(self, 'init_menu_func', types.MethodType(func, self))

    def _init_env(self):
        if hasattr(self, 'init_actions_func'):
            self.init_actions_func()
        if hasattr(self, 'init_menu_func'):
            self.init_menu_func()
        if hasattr(self, 'init_docks_func'):
            self.init_docks_func()
        if hasattr(self, 'init_connect_func'):
            self.init_connect_func()
        if hasattr(self, 'init_signal_func'):
            self.init_signal_func()

    def run(self):
        self._init_env()
        self.mainwindow.showMaximized()
        self.mainwindow.show()
        if hasattr(self, 'splash'):
            self.splash.finish(self.mainwindow)
        self.app.exec_()
