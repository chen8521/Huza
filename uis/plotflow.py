# coding=utf-8
import re, os, time, codecs
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from loguru import logger
from auto_ui.plotflow import Ui_Form


class PlotFlow_Form(Ui_Form):

    def __init__(self, extra):
        self.extra = extra

    def setupUi(self, Form):
        self.form = Form
        super(PlotFlow_Form, self).setupUi(Form)
        self.load()
        self.connect()

    def load(self):
        self.tabWidget.tabCloseRequested.connect(self.close_current_tab)

    def close_current_tab(self, i):
        if self.tabWidget.count() < 2:
            return
        self.tabWidget.removeTab(i)
    def connect(self):
        pass
