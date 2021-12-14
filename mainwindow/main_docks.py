from PyQt5.QtCore import QSize, Qt, pyqtSignal
from PyQt5.QtWidgets import QDockWidget, QWidget, QLabel, QTextEdit

from util.register import MainQWidget


def loadalldocks(self):
    self.form.setDockNestingEnabled(True)
    self.form.takeCentralWidget()

    self.docks["main"] = QDockWidget("")
    self.docks["main"].setMinimumSize(QSize(700, 200))
    self.docks["main"].setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)

    self.docks["para"] = QDockWidget("")
    self.docks["para"].setMinimumWidth(280)
    self.docks["para"].setMinimumHeight(300)
    self.docks["para"].setFeatures(QDockWidget.AllDockWidgetFeatures)

    self.docks["setup"] = QDockWidget("参数")
    self.docks["setup"].setMinimumWidth(350)
    self.docks["setup"].setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
    self.docks["setup"].setVisible(False)

    self.docks["info"] = QDockWidget("输出")
    self.docks["info"].setMaximumHeight(300)
    self.docks["info"].setMinimumHeight(200)
    self.docks["info"].setFeatures(QDockWidget.AllDockWidgetFeatures)
    self.docks["info"].setVisible(False)

    self.form.addDockWidget(Qt.LeftDockWidgetArea, self.docks["para"])

    self.form.splitDockWidget(self.docks["para"], self.docks["setup"], Qt.Horizontal)
    self.form.splitDockWidget(self.docks["setup"], self.docks["main"], Qt.Horizontal)
    self.form.splitDockWidget(self.docks["main"], self.docks["info"], Qt.Vertical)

    w = QTextEdit()
    # w.setStyleSheet('QLabel { background-color : red; color : blue; }')
    self.docks["info"].setWidget(w)


def addMain(self, Form):
    contianerWidget = MainQWidget(self.form)
    ui = Form(extra=self.extra)
    ui.setupUi(contianerWidget)
    contianerWidget._ui = ui
    return contianerWidget


def setMainView(self, name, displayname, formclass):
    if self.docks["main"].windowTitle() == name:
        return
    self.setDockName('main', displayname)

    if name in self.mains:
        w = self.mains[name]
        self.docks["main"].setWidget(w)
    else:
        contianerWidget = self.addMain(formclass)
        self.setDockName('main', displayname)
        self.docks["main"].setWidget(contianerWidget)
        self.mains[name] = contianerWidget


def setSetupView(self, name, displayname, formclass):
    if self.docks["setup"].windowTitle() == name:
        return
    self.setDockName('setup', displayname)

    if name in self.setups:
        w = self.setups[name]
        self.docks["setup"].setWidget(w)
    else:
        contianerWidget = self.addMain(formclass)
        contianerWidget.signal.connect(self.signalHeadle)
        self.setDockName('setup', displayname)
        self.docks["setup"].setWidget(contianerWidget)
        self.setups[name] = contianerWidget


def setParaView(self, action, formclass, databind=None):
    name = action.text()
    myactionname = action.myactionname
    if self.docks["para"].windowTitle() == name:
        return
    self.setDockName('para', name)

    para_widget = self.docks['para'].widget()
    if para_widget is not None:
        self.last_para = para_widget.myactionname

    class MyQWidget(QWidget):
        signal = pyqtSignal(object, object)

        def ui(self):
            if hasattr(self, '_ui'):
                return self._ui

    if myactionname in self.paras and myactionname not in self.exclude_para:
        w = self.paras[myactionname]
        self.docks["para"].setWidget(w)
        if hasattr(w, 'myrefresh'):
            w.myrefresh()
    else:
        w = MyQWidget(self.form)
        w.signal.connect(self.signalHeadle)
        if databind is not None and isinstance(databind, dict):
            ui = formclass(self.extra)
            for k, v in databind.items():
                setattr(ui, k, v)
        else:
            ui = formclass(self.extra)
        ui.setupUi(w)
        w._ui = ui
        w.myactionname = myactionname
        w.myname = name
        self.docks["para"].setWidget(w)
        self.paras[action.myactionname] = w
