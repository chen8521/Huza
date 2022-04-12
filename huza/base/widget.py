from PyQt5 import QtGui
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QItemDelegate, QPushButton, QHBoxLayout, QTableView, QDialog
from loguru import logger


class MainQWidget(QWidget):
    signal = pyqtSignal(object, object)
    keypresssignal = pyqtSignal(object)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        self.keypresssignal.emit(a0)
        super(MainQWidget, self).keyPressEvent(a0)

    def ui(self):
        if hasattr(self, '_ui'):
            return self._ui
        return None


class PopQDialog(QDialog):
    signal = pyqtSignal(object, object)
