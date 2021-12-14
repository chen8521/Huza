# coding=utf-8
import re, os, time, codecs
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QHeaderView, QItemDelegate, QPushButton, QHBoxLayout, QWidget
from loguru import logger
from auto_ui.filelist import Ui_Form
from util.constant import SINGNAL_SHOW_TEXT


class MyQStandardItemModelModel(QStandardItemModel):
    def data(self, index, role=None):
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        return QStandardItemModel.data(self, index, role)


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

            button_view.index = index
            h_box_layout = QHBoxLayout()
            h_box_layout.addWidget(button_view)
            h_box_layout.setContentsMargins(0, 0, 0, 0)
            h_box_layout.setAlignment(Qt.AlignCenter)
            widget = QWidget()
            widget.setLayout(h_box_layout)
            self.parent().setIndexWidget(
                index,
                widget
            )


class FileList_Form(Ui_Form):

    def __init__(self, extra):
        self.extra = extra

    def setupUi(self, Form):
        self.form = Form
        super(FileList_Form, self).setupUi(Form)
        self.load()
        self.connect()

    def mylistdir(self):
        if os.path.exists('2d'):
            project = 'projects'
        if os.path.exists('3d'):
            project = 'projects2'
        _list = []
        for i in os.listdir(project):
            _list.append(i)
        return _list

    def load(self):
        self.tableView.setItemDelegateForColumn(1, EditDeleteDelegate(self.tableView))
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.ViewClicked = self.ViewClicked
        self.tableView.setColumnWidth(1, 100)
        self.adddata()

    def adddata(self):
        grid_model = MyQStandardItemModelModel()
        grid_model.setHorizontalHeaderLabels(['文件名', '操作'])

        for _i, i in enumerate(self.mylistdir()):
            num_item = QStandardItem(i)
            num_item.setData(i, 1)
            grid_model.appendRow([
                num_item,
            ])
        self.tableView.setModel(grid_model)

    def ViewClicked(self):
        index = self.tableView.sender().index
        row = index.row()  # ModelIndex
        data = self.tableView.model().index(row, 0).data(1)  # GridSchema
        self.form.signal.emit(SINGNAL_SHOW_TEXT, data)

    def connect(self):
        pass
