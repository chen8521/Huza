# coding=utf-8

from huza.mainwindow.main_actions import *
from huza.mainwindow.main_docks import *
from huza.mainwindow.main_ribbon import *
from huza.slots.main_welcome import *
from huza.slots.main_chart import *
from huza.slots.main_text import *
from huza.ribbon.RibbonWidget import RibbonWidget
from huza.slots.main_setting import *
from huza.slots.main_action_trigger import *

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
        self.last_para = None
        self.last_main = None
        self.exclude_para = ['coordinate_textedit']  # 不保留缓存，每次都初始化
        self.last_lenth = 0
        self.slice_flag = 0
        self.last_2d_index = 0
        self.load()
        self.connect()

    def addSig(self, sig, func):
        self.signals[sig] = func

    loadalldocks = loadalldocks
    createActions = createActions
    init_ribbon = init_ribbon
    connectAction = connectAction
    addMain = addMain
    setMainView = setMainView
    addSig = addSig
    setParaView = setParaView
    setSetupView = setSetupView
    addWelcome = addWelcome
    solt_action_help_about = solt_action_help_about
    solt_action_help_doc = solt_action_help_doc
    solt_action_coordinate_legend = solt_action_coordinate_legend
    solt_action_coordinate_textedit = solt_action_coordinate_textedit
    setChartAction = setChartAction
    solt_action_coordinate_zoom = solt_action_coordinate_zoom
    solt_action_coordinate_zoom_reset = solt_action_coordinate_zoom_reset
    solt_action_coordinate_move = solt_action_coordinate_move
    solt_action_coordinate_save = solt_action_coordinate_save
    solt_action_coordinate_set = solt_action_coordinate_set
    solt_action_gendemo = solt_action_gendemo
    setChartMode = setChartMode
    setText2 = setText2
    setRest = setRest
    setSaveFigure = setSaveFigure
    setLagendEnable = setLagendEnable
    ChageSetting = ChageSetting
    ChangeMesh = ChangeMesh
    rems_plot_contourf_xy = rems_plot_contourf_xy
    quxian = quxian
    quxian2 = quxian2
    sandian = sandian
    sample = sample
    quxian3 = quxian3
    heatmap = heatmap
    yun = yun
    hexbin = hexbin
    times = times
    yun2 = yun2
    td = td
    td2 = td2
    movea = movea
    readstl = readstl
    readmesh = readmesh
    bind_action_slot = bind_action_slot
    ImportMesh = ImportMesh
    def load(self):
        self.createActions()
        self.addRibbon()
        self.loadalldocks()
        self.loaddefaultStatus()
        self.registerSignal()
        self.bindCloseEvent()

    def bindCloseEvent(self):
        def closeprocess():
            if hasattr(self, 'vtkWidget'):
                self.vtkWidget.Finalize()
            if hasattr(self, 'vtkWidget2'):
                self.vtkWidget2.Finalize()

        self.form.closeprocess = closeprocess

    def registerSignal(self):
        self.adddemo()

    def adddemo(self):
        self.addSig('quxian', self.quxian)
        self.addSig('quxian2', self.quxian2)
        self.addSig('sandian', self.sandian)
        self.addSig('sample', self.sample)
        self.addSig('quxian3', self.quxian3)
        self.addSig('heatmap', self.heatmap)
        self.addSig('yun', self.yun)
        self.addSig('yun2', self.yun2)
        self.addSig('hexbin', self.hexbin)
        self.addSig('times', self.times)
        self.addSig('td', self.td)
        self.addSig('td2', self.td2)
        self.addSig('movea', self.movea)
        self.addSig('readstl', self.readstl)
        self.addSig('readmesh', self.readmesh)

    def setlastparadock(self, args):
        if self.last_para is not None and self.last_para in self.paras:
            w = self.paras[self.last_para]
            self.setDockName('para', self.paras[self.last_para].myname)
            self.docks["para"].setWidget(w)

    def loaddefaultStatus(self):
        if not self.extra.debug:
            pass
        self.docks['para'].setVisible(False)
        self.actions["showpara"].setChecked(False)
        self.actions["showsetup"].setChecked(False)
        self.addWelcome()

    def signalHeadle(self, key, args):
        if key in self.signals:
            self.signals[key](args)

    def addRibbon(self):
        self.form._ribbon = RibbonWidget(self.form)
        self.form.addToolBar(self.form._ribbon)
        self._ribbon = self.form._ribbon
        self._ribbon._ribbon_widget.tabBarClicked.connect(self.tabChange)
        self.init_ribbon()

    def tabChange(self, tab_index):
        text = self._ribbon._ribbon_widget.tabText(tab_index)

    def tr(self, *args, **kwargs):
        return self.form.tr(*args, **kwargs)

    def setDockName(self, dock, name):
        self.docks[dock].setWindowTitle(name)
        self.docks[dock].setVisible(True)

    def connect(self):
        self.connectAction()
        self.docks["para"].visibilityChanged.connect(self.actions["showpara"].setChecked)
        self.docks["setup"].visibilityChanged.connect(self.actions["showsetup"].setChecked)
        self.docks["info"].visibilityChanged.connect(self.actions["showinfo"].setChecked)
