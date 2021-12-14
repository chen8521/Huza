# coding=utf-8
from auto_ui.create_materials import Ui_Form


class CreateMaterials_Form(Ui_Form):

    def __init__(self, extra):
        self.extra = extra

    def setupUi(self, Form):
        self.form = Form
        super(CreateMaterials_Form, self).setupUi(Form)
        self.load()
        self.connect()

    def load(self):
        pass

    def connect(self):
        pass
