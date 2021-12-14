# coding=utf-8
from PyQt5.QtWidgets import QDialog
from auto_ui.bjtjsz import Ui_Form
from uis.profiles import Profiles_Form


class Setting_BJTJSZ_Form(Ui_Form):

    def __init__(self, extra):
        self.extra = extra

    def setupUi(self, Form):
        self.form = Form
        super(Setting_BJTJSZ_Form, self).setupUi(Form)
        self.load()
        self.connect()

    def load(self):
        pass

    def profiles(self):
        self.widget_mesh2 = QDialog(self.form)
        self.ui_mesh2 = Profiles_Form(self.extra)
        self.ui_mesh2.setupUi(self.widget_mesh2)
        self.widget_mesh2.exec()

    def connect(self):
        self.pushButton_profiles.clicked.connect(self.profiles)
