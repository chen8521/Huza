from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel


class MyQStandardItemModelModel(QStandardItemModel):
    def data(self, index, role=None):
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        return QStandardItemModel.data(self, index, role)
