from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QItemDelegate, QPushButton, QHBoxLayout, QTableView
from loguru import logger


class MainQWidget(QWidget):
    signal = pyqtSignal(object, object)

    def ui(self):
        if hasattr(self, '_ui'):
            return self._ui
        return None



