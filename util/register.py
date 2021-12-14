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


def addSig(self, sig, func):
    self.signals[sig] = func

class EditDeleteDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super(EditDeleteDelegate, self).__init__(parent)

    def default_click(self):
        pass

    def paint(self, painter, option, index):
        if not self.parent().indexWidget(index):
            button_view = QPushButton(
                self.tr('查看'),
                self.parent(),
                clicked=self.parent().ViewClicked if hasattr(self.parent(), 'ViewClicked') else self.default_click
            )
            icon1 = QIcon()
            icon1.addPixmap(QPixmap(":/db/属性表108.svg"), QIcon.Normal, QIcon.Off)
            button_view.setIcon(icon1)

            button_edit = QPushButton(
                self.tr('编辑'),
                self.parent(),
                clicked=self.parent().EditClicked if hasattr(self.parent(), 'EditClicked') else self.default_click
            )
            icon1 = QIcon()
            icon1.addPixmap(QPixmap(":/db/缺省属性483.svg"), QIcon.Normal, QIcon.Off)
            button_edit.setIcon(icon1)


            button_delete = QPushButton(
                self.tr('删除'),
                self.parent(),
                clicked=self.parent().DeleteClicked if hasattr(self.parent(), 'DeleteClicked') else self.default_click
            )
            icon1 = QIcon()
            icon1.addPixmap(QPixmap(":/img/fit/tuichu.svg"), QIcon.Normal, QIcon.Off)
            button_delete.setIcon(icon1)

            button_edit.index = index
            button_delete.index = index
            button_view.index = index
            h_box_layout = QHBoxLayout()
            h_box_layout.addWidget(button_view)
            h_box_layout.addWidget(button_edit)
            h_box_layout.addWidget(button_delete)
            h_box_layout.setContentsMargins(0, 0, 0, 0)
            h_box_layout.setAlignment(Qt.AlignCenter)
            widget = QWidget()
            widget.setLayout(h_box_layout)
            self.parent().setIndexWidget(
                index,
                widget
            )
