# coding=utf-8
import re, os, time, codecs
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QTreeWidgetItem
from loguru import logger
from auto_ui.navigate import Ui_Form
from huza.base.dockview import DockView


class NaviGate_Form(Ui_Form, DockView):

    def setupUi(self, Form):
        self.form = Form
        super(NaviGate_Form, self).setupUi(Form)
        self.load()
        self.connect()

    def load(self):
        self.add_tree()

    def connect(self):
        pass

    def add_setting(self, root):
        def add_set(name, flag, icon):
            setting = QTreeWidgetItem(root)
            setting.flag = flag
            setting.setText(0, name)
            setting.setIcon(0, icon)

        root.setExpanded(True)
        add_set('湍流模型', 1, self.iconlist.default.cot550)
        add_set('多相流模型', 2, self.iconlist.default.cot550)
        add_set('介质特性设置', 3, self.iconlist.default.cot550)

    def click(self, item):
        if not hasattr(item, 'flag'):
            return
        flag = item.flag
        if flag == 1:
            self.emit('a1', item)
        elif flag == 2:
            self.emit('a2', item)
        elif flag == 3:
            self.emit('a3', item)
        elif flag == 4:
            self.emit('a4', item)

    def add_tree(self):
        self.treeWidget_nav.setColumnCount(1)
        self.treeWidget_nav.itemClicked.connect(self.click)
        self.treeWidget_nav.header().setVisible(False)
        mesh = QTreeWidgetItem(self.treeWidget_nav)
        self.mesh = mesh
        mesh.flag = 4
        mesh.setText(0, f'网格导入')
        mesh.setIcon(0, self.iconlist.default.cot550)
        mesh.setExpanded(True)

        setting = QTreeWidgetItem(self.treeWidget_nav)
        self.setting = setting
        setting.setText(0, f'参数设置')
        setting.setIcon(0, self.iconlist.default.cot550)
        self.add_setting(setting)

        run = QTreeWidgetItem(self.treeWidget_nav)
        self.run = run
        run.setText(0, f'计算')
        run.setIcon(0, self.iconlist.default.cot550)
        run.setExpanded(True)

        run2 = QTreeWidgetItem(run)
        run2.setText(0, f'开始计算')
        run2.setIcon(0, self.iconlist.default.cot550)

        result = QTreeWidgetItem(self.treeWidget_nav)
        self.result = result
        result.setText(0, f'结果查看')
        result.setIcon(0, self.iconlist.default.cot550)
