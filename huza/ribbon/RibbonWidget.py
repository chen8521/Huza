from PyQt5.QtWidgets import *

from huza.ribbon.RibbonTab import RibbonTab
from huza.ribbon.qss.ribbonqss import ribbonqss
from huza.ribbon.scale import gui_scale


class RibbonWidget(QToolBar):
    def __init__(self, parent):
        QToolBar.__init__(self, parent)
        self.setStyleSheet(ribbonqss)
        self.setObjectName("ribbonWidget")
        self.setWindowTitle("Ribbon")
        self._ribbon_widget = QTabWidget(self)
        self._ribbon_widget.setMaximumHeight(120 * gui_scale())
        self._ribbon_widget.setMinimumHeight(110 * gui_scale())
        self.setMovable(False)
        self.addWidget(self._ribbon_widget)

    def add_ribbon_tab(self, name):
        ribbon_tab = RibbonTab(self, name)
        ribbon_tab.setObjectName("tab_" + name)
        self._ribbon_widget.addTab(ribbon_tab, name)
        return ribbon_tab

    def set_active(self, name):
        self.setCurrentWidget(self.findChild("tab_" + name))
