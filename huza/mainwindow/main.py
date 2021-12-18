# coding=utf-8

from huza.mainwindow.main_actions import *
from huza.mainwindow.main_docks import *
from huza.mainwindow.main_ribbon import *
from huza.ribbon.RibbonWidget import RibbonWidget


class MainWindow_Form(object):

    def __init__(self, extra):
        self.extra = extra
        super(MainWindow_Form, self).__init__()

    def setupUi(self, Form):
        self.form = Form
        self.docks = {}
        self.actions = {}
        self.signals = {}
        self.paras = {}  # 保存设置页的所有参数
        self.mains = {}  # 保存所有的主页的界面对象
        self.setups = {}  # 保存所有的主页的界面对象
        self.load()
        self.connect()

    def addSig(self, sig, func):
        self.signals[sig] = func

    init_ribbon = init_ribbon
    init_docks = init_docks
    addMain = addMain
    setMainView = setMainView
    addSig = addSig
    setParaView = setParaView
    setSetupView = setSetupView
    addAction = addAction

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

    def connect(self):
        pass
        # self.docks["para"].visibilityChanged.connect(self.actions["showpara"].setChecked)
        # self.docks["setup"].visibilityChanged.connect(self.actions["showsetup"].setChecked)
        # self.docks["info"].visibilityChanged.connect(self.actions["showinfo"].setChecked)
