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
        self.dockviews[k] = {}
    for l in layout:
        hand = l[0]
        if hand == DOCK_LAYOUT_ADD:
            _, oriz, dockname = l
            self.form.addDockWidget(DockWidgetAreadict[oriz], self.docks[dockname])
        elif hand == DOCK_LAYOUT_SPLIT:
            _, d1, d2, ori = l
            self.form.splitDockWidget(self.docks[d1], self.docks[d2], Orientiondict[ori])


def setDockView(self, name, displayname, dockname, formclass):
    dock = self.docks.get(dockname)
    if dock.windowTitle() == name:
        return
    dock.setWindowTitle(displayname)
    dock.setVisible(True)
    dockviews = self.dockviews[dockname]
    if name in dockviews:
        w = dockviews.get(name)
        dock.setWidget(w)
        if hasattr(w, 'refresh'):
            w.refresh()
        return w.ui()
    else:
        w = MainQWidget(self.form)
        w.signal.connect(self.signalHeadle)
        ui = formclass(self)
        ui._name_sig = name  # 用于标记名称
        ui.setupUi(w)
        w._ui = ui
        dock.setWidget(w)
        dockviews[name] = w
        return ui
