# coding=utf-8
import re, os, time, codecs
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from loguru import logger
from auto_ui.bjtjsz import Ui_Form
from huza.base.dockview import DockView


class BJTJSZ_Form(Ui_Form, DockView):

    def setupUi(self, Form):
        self.form = Form
        super(BJTJSZ_Form, self).setupUi(Form)
        self.load()
        self.connect()

    def load(self):
        pass

    def connect(self):
        pass
