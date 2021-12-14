# coding=utf-8

from auto_ui.main import Ui_MainWindow
from slots.flow_view import flow_view
from mainwindow.main_actions import *
from mainwindow.main_docks import *
from mainwindow.main_ribbon import *
from slots.main_welcome import *
from slots.main_chart import *
from slots.main_text import *
from util.register import *
from util.ribbon.RibbonWidget import RibbonWidget
from slots.main_setting import *
from slots.mesh_view import *
from slots.run_calcu import *
from slots.showtext import *
from slots.main_action_trigger import *

class MainWindow_Form(Ui_MainWindow):
    _ = MyNavigationToolbar2QT  # 确保不会被删除引用

    def __init__(self, extra):
        self.extra = extra
        super(MainWindow_Form, self).__init__()

    def setupUi(self, Form):
        self.form = Form
        super(MainWindow_Form, self).setupUi(Form)
        self.form.resize(1280, 800)
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
    solt_action_help_version = solt_action_help_version
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
    solt_action_szmn = solt_action_szmn
    solt_action_meshimport = solt_action_meshimport
    ImportMesh = ImportMesh
    run_calc = run_calc
    drawplot = drawplot
    addpost = addpost
    showfilelist = showfilelist
    ShowText = ShowText
    loadtext = loadtext
    flow_view = flow_view
    addMeshTools = addMeshTools
    stop_calc = stop_calc
    run_calc_2d = run_calc_2d
    run_calc_3d = run_calc_3d
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
        self.addSig(SINGNAL_CHANGE_SETTING, self.ChageSetting)
        self.addSig(SINGNAL_CHANGE_MESH, self.ChangeMesh)
        self.addSig(SINGNAL_IMPORT_MESH, self.ImportMesh)
        self.addSig(SINGNAL_RUN, self.run_calc)
        self.addSig(SINGNAL_STOP, self.stop_calc)
        self.addSig(SINGNAL_SHOW_FILE_LIST, self.showfilelist)
        self.addSig(SINGNAL_SHOW_TEXT, self.ShowText)
        self.addSig(SINGNAL_FLOW_VIEW, self.flow_view)

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
