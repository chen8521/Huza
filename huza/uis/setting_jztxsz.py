# coding=utf-8
from PyQt5.QtWidgets import QDialog
from auto_ui.jztzsz import Ui_Form
from uis.mertrals import CreateMaterials_Form


class Setting_JZTXSZ_Form(Ui_Form):

    def __init__(self, extra):
        self.extra = extra

    def setupUi(self, Form):
        self.form = Form
        super(Setting_JZTXSZ_Form, self).setupUi(Form)
        self.load()
        self.connect()

    def load(self):
        pass
    def meradd(self):
        self.widget_mesh = QDialog(self.form)
        self.ui_mesh = CreateMaterials_Form(self.extra)
        self.ui_mesh.setupUi(self.widget_mesh)
        self.widget_mesh.exec()
    def connect(self):
        self.pushButton_addmer.clicked.connect(self.meradd)
