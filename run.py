# coding=utf-8
import os
import types

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QDockWidget, QTextEdit, QAction
from loguru import logger

from huza.base.mainwindow_run import MainWindowRun
from huza.mainwindow import MainWindow_Form
from huza.util.buildui import build_uidir
from huza.util.mainui import get_dock_ui
from uis.bjtjsz import BJTJSZ_Form
from uis.dxlmx import DXLMX_Form
from uis.jztzsz import JZTZSZ_Form
from uis.navigate import NaviGate_Form


class Extra:
    debug = None

    def __init__(self, debug=False):
        self.debug = debug


DEBUG = True

if 'DEBUG_MODE' in os.environ:
    DEBUG = True


def init_actions(obj):
    obj.addAction('showsetup', '设置面板', '显示/隐藏设置面板', checkable=True, icon=obj.icon_list.default.Adddata6)
    obj.addAction('showpara', '导航面板', '显示/隐藏导航面板', checkable=True, icon=obj.icon_list.default.cot550)
    obj.addAction('showinfo', '信息面板', '显示/隐藏信息面板', checkable=True, icon=obj.icon_list.default.bim439)
    obj.addAction('exit', '退出', '退出', icon=obj.icon_list.default.Stop37)
    obj.addAction('t1', 't1', icon=obj.icon_list.default.Unit220)
    obj.addAction('t2', 't2', icon=obj.icon_list.default.Zoom100)


def init_menu(obj):
    c = {'开始': [
        {'测试': [('t1', True), ('t2', True)]},
        {'关闭': [('exit', True)]}
    ],
        '视图': [
            {'视图控制': ['showsetup', 'showpara', 'showinfo']},
        ],
    }
    obj.init_menu(c)


def init_docks(obj):
    d1 = QDockWidget("1")
    d1.setMinimumSize(QSize(700, 200))
    d1.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)

    d2 = QDockWidget("2")
    d2.setMinimumWidth(280)
    d2.setMinimumHeight(300)
    d2.setFeatures(QDockWidget.AllDockWidgetFeatures)

    d3 = QDockWidget("3")
    d3.setMinimumWidth(350)
    d3.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)

    d4 = QDockWidget("4")
    d4.setMaximumHeight(400)
    d4.setFeatures(QDockWidget.AllDockWidgetFeatures)
    docks = {
        'main': d1,
        'para': d2,
        'setup': d3,
        'info': d4,
    }
    layout = [('add', 'left', 'para'),
              ('split', 'para', 'setup', 'h'),
              ('split', 'setup', 'main', 'h'),
              ('split', 'main', 'info', 'v'),
              ]
    obj.init_docks(docks, layout)


def init_connect(self):
    exit = self.get_action('exit')
    exit.triggered.connect(self.mainwindow.close)

    showpara = self.get_action('showpara')
    para_dock = self.get_dock('para')
    para_dock.visibilityChanged.connect(showpara.setChecked)
    showpara.triggered.connect(para_dock.setVisible)

    showinfo = self.get_action('showinfo')
    info_dock = self.get_dock('info')
    info_dock.visibilityChanged.connect(showinfo.setChecked)
    showinfo.triggered.connect(info_dock.setVisible)

    t1 = self.get_action('t1')

    def navi():
        self.set_dock_view('navi', '功能', 'para', NaviGate_Form)

    t1.triggered.connect(navi)


def a(mainui: MainWindow_Form, arg):
    mainui.setDockView('jztzsz', 'JZTZSZ', 'setup', JZTZSZ_Form)


def b(mainui: MainWindow_Form, arg):
    mainui.setDockView('bjtjsz', 'BJTJSZ', 'setup', BJTJSZ_Form)


def c(mainui: MainWindow_Form, arg):
    mainui.setDockView('dxlmx', 'DXLMX', 'setup', DXLMX_Form)


def d(mainui: MainWindow_Form, arg):
    ui = get_dock_ui(mainui, 'setup', 'dxlmx')
    ui.checkBox_2.setText('fffffffffffffffffff')


def init_signal(app):
    app.bind_signal('a1', a)
    app.bind_signal('a2', b)
    app.bind_signal('a3', c)
    app.bind_signal('a4', d)


if __name__ == '__main__':
    if DEBUG:
        build_uidir('ui_file', 'auto_ui')
    extra = Extra(debug=DEBUG)
    app = MainWindowRun(extra)
    app.set_window_logo(app.icon_list.default.Calculatehortestpath_grid_671)
    app.set_window_title('测试')
    app.set_init_actions_func(init_actions)
    app.set_init_menu_func(init_menu)
    app.set_init_docks_func(init_docks)
    app.set_init_connect_func(init_connect)
    app.set_init_signal_func(init_signal)
    app.run()
