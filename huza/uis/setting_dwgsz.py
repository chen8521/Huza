# coding=utf-8
import re, os, time, codecs
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from loguru import logger
from auto_ui.dwgsz import Ui_Form


class Setting_DWGSZ_Form(Ui_Form):

    def __init__(self, extra):
        self.extra = extra

    def setupUi(self, Form):
        self.form = Form
        super(Setting_DWGSZ_Form, self).setupUi(Form)
        self.load()
        self.connect()

    def load(self):
        pass
    def connect(self):
        pass
