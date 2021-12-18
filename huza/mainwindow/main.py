# coding=utf-8

from huza.mainwindow.main_actions import *
from huza.mainwindow.main_docks import *
from huza.mainwindow.main_ribbon import *
from huza.ribbon.RibbonWidget import RibbonWidget
from huza.util.mainui import *

class MainWindow_Form(object):
    init_ribbon = init_ribbon
    init_docks = init_docks
    addAction = addAction
    setDockView = setDockView
    get_extra = get_extra
    get_action = get_action
    get_dock = get_dock
    get_dock_current_ui = get_dock_current_ui
    get_dock_ui = get_dock_ui
    def __init__(self, extra, icon_list):
        self.extra = extra
        self.icon_list = icon_list
        super(MainWindow_Form, self).__init__()

    def setupUi(self, Form):
        self.form = Form
        self.docks = {}
        self.actions = {}
        self.signals = {}
        self.dockviews = {}  # 保存所有dock里面的widget对象
        self.load()

    def bind_signal(self, signal, func):
        self.signals[signal] = func

    def load(self):
        self.addRibbon()
        self._init_dock_env()

    def signalHeadle(self, key, args):
        if key in self.signals:
            self.signals[key](args)

    def addRibbon(self):
        self.form._ribbon = RibbonWidget(self.form)
        self.form.addToolBar(self.form._ribbon)
        self._ribbon = self.form._ribbon

    def _init_dock_env(self):
        self.form.setDockNestingEnabled(True)
        w = self.form.takeCentralWidget()
        if w:
            del w
