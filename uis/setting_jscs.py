# coding=utf-8
import re, os, time, codecs
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from loguru import logger
from auto_ui.jscs import Ui_Form
from util.constant import *


class Setting_JSCS_Form(Ui_Form):

    def __init__(self, extra):
        self.extra = extra

    def setupUi(self, Form):
        self.form = Form
        super(Setting_JSCS_Form, self).setupUi(Form)
        self.load()
        self.connect()

    def load(self):
        self.pushButton_stop.setEnabled(False)

    def runa(self):
        self.form.signal.emit(SINGNAL_RUN, 0)

    def stop(self):
        self.form.signal.emit(SINGNAL_STOP, 0)

    def connect(self):
        self.pushButton_run.clicked.connect(self.runa)
        self.pushButton_stop.clicked.connect(self.stop)
