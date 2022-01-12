# coding=utf-8
import re, os, time, codecs
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QApplication, QVBoxLayout, QLineEdit, QWidget, QHBoxLayout, \
    QLabel
from loguru import logger
from auto_ui.showicon import Ui_Form
from huza.base.dockview import DockView


class ShowIcon_Form(Ui_Form, DockView):

    def setupUi(self, Form):
        self.form = Form
        super(ShowIcon_Form, self).setupUi(Form)
        self.load()
        self.connect()

    def load(self):
        for j in list(self.iconlist._iconlist.keys()) + ['default']:
            qvbox = QVBoxLayout()
            qhbox = QHBoxLayout()
            label = QLabel()
            label.setText('搜索：')
            line = QLineEdit()
            line.setMaximumWidth(300)
            all_icon_names = list(getattr(self.iconlist, j)._icon_database.keys())
            icon_j = getattr(self.iconlist, j)

            def itemChange(text):
                listWidget = self.tabWidget.currentWidget().findChild(QListWidget)
                all_icon_names = listWidget.all_icon_names
                icon_j = listWidget.icon_j
                listWidget.clear()
                if text.strip() == '':
                    all_icon_names2 = all_icon_names
                else:
                    all_icon_names2 = []
                    for j1 in all_icon_names:
                        if text.lower() in j1.lower():
                            all_icon_names2.append(j1)
                for i in all_icon_names2:
                    item = QListWidgetItem(getattr(icon_j, i), i)
                    item.setToolTip(i)
                    item.setSizeHint(QSize(80, 80))
                    item._text = f'{j}.{i}'
                    listWidget.addItem(item)

            line.textChanged.connect(itemChange)
            qhbox.addWidget(label)
            qhbox.addWidget(line)
            qhbox.addStretch()
            qvbox.addLayout(qhbox)
            listWidget = QListWidget()
            listWidget.all_icon_names = all_icon_names
            listWidget.icon_j = icon_j
            qvbox.addWidget(listWidget)
            listWidget.setIconSize(QSize(60, 60))
            listWidget.setResizeMode(QListWidget.Adjust)
            listWidget.setViewMode(QListWidget.IconMode)
            listWidget.setMovement(QListWidget.Static)
            listWidget.setSpacing(10)

            for i in all_icon_names:
                item = QListWidgetItem(getattr(getattr(self.iconlist, j), i), i)
                item.setToolTip(i)
                item.setSizeHint(QSize(80, 80))
                item._text = f'{j}.{i}'
                listWidget.addItem(item)

            listWidget.itemDoubleClicked.connect(self.click)
            qw = QWidget()
            qw.setLayout(qvbox)
            self.tabWidget.addTab(qw, j)

    def click(self, item):
        _text = item._text
        clipboard = QApplication.clipboard()
        clipboard.setText(_text)

    def connect(self):
        pass
