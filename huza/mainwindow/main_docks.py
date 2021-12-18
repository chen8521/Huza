from PyQt5.QtCore import QSize, Qt, pyqtSignal
from PyQt5.QtWidgets import QDockWidget, QWidget, QLabel, QTextEdit

from huza.base.widget import MainQWidget
from huza.util.constant import *


def init_docks(self, docks: dict, layout: list):
    """docks = {
        'main': QDockWidget(""),
        'para': QDockWidget(""),
        'setup': QDockWidget(""),
        'info': QDockWidget(""),
    }
    layout = [('add', 'left', 'para'),
         ('split', 'para', 'setup', 'h'),
         ('split', 'setup', 'main', 'h'),
         ('split', 'main', 'info', 'v'),
         ]

    :param self:
    :type self:
    :param docks_dict:
    :type docks_dict:
    :return:
    :rtype:
    """
    for k, v in docks.items():
        self.docks[k] = v
    for l in layout:
        hand = l[0]
        if hand == DOCK_LAYOUT_ADD:
            _, oriz, dockname = l
            self.form.addDockWidget(DockWidgetAreadict[oriz], self.docks[dockname])
        elif hand == DOCK_LAYOUT_SPLIT:
            _, d1, d2, ori = l
            self.form.splitDockWidget(self.docks[d1], self.docks[d2], Orientiondict[ori])






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
