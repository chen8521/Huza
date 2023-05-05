from qtpy import QtGui
from qtpy.QtCore import Qt, Signal
from qtpy.QtGui import QIcon, QPixmap
from qtpy.QtWidgets import QWidget, QItemDelegate, QPushButton, QHBoxLayout, QTableView, QDialog
from loguru import logger


class MainQWidget(QWidget):
    signal = Signal(object, object)
    keypresssignal = Signal(object)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        self.keypresssignal.emit(a0)
        super(MainQWidget, self).keyPressEvent(a0)

    def ui(self):
        if hasattr(self, '_ui'):
            return self._ui
        return None


class PopQDialog(QDialog):
    signal = Signal(object, object)
