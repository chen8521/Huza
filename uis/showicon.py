# coding=utf-8
import re, os, time, codecs
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QApplication
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
        self.listWidget.setIconSize(QSize(60, 60))
        self.listWidget.setResizeMode(QListWidget.Adjust)
        self.listWidget.setViewMode(QListWidget.IconMode)
        self.listWidget.setMovement(QListWidget.Static)
        self.listWidget.setSpacing(10)
        all_icon_names = list(self.iconlist.default._icon_database.keys())
        for i in all_icon_names:
            if len(i) >= 15:
                _i = i[:12] + '...'
            else:
                _i = i
            item = QListWidgetItem(getattr(self.iconlist.default, i), _i)
            item.setSizeHint(QSize(80, 80))
            item._text = i
            self.listWidget.addItem(item)

    def click(self, item):
        _text = item._text
        clipboard = QApplication.clipboard()
        clipboard.setText(_text)

    def connect(self):
        self.listWidget.itemDoubleClicked.connect(self.click)
