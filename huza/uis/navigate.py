# coding=utf-8
import re, os, time, codecs
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QTreeWidgetItem
from loguru import logger
from auto_ui.navigate import Ui_Form
from util.constant import *


class Navigate_Form(Ui_Form):

    def __init__(self, extra):
        self.extra = extra

    def setupUi(self, Form):
        self.form = Form
        super(Navigate_Form, self).setupUi(Form)
        self.load()
        self.connect()

    def load(self):
        self.add_tree()

    def connect(self):
        pass

    def item_click(self, item):
        parent = item.parent()

        def setitemblod():
            self.clear_all_select(parent)
            item.setText(0, item.text(0) + '[*]')
            font = QFont()
            font.setBold(True)
            item.setFont(0, font)

        if hasattr(parent, 'flag') and parent.flag == FLAG_SETTING:
            self.form.signal.emit(SINGNAL_CHANGE_SETTING, item)
        if hasattr(parent, 'flag') and parent.flag in (FLAG_SETTING,):
            setitemblod()
        if hasattr(parent, 'flag') and parent.flag == FLAG_MESH:
            self.form.signal.emit(SINGNAL_CHANGE_MESH, item)
        if hasattr(item, 'flag') and item.flag == FLAG_MESH:
            self.form.signal.emit(SINGNAL_IMPORT_MESH, item)

        if hasattr(item, 'flag') and item.flag == FLAG_RUN_LIST:
            self.form.signal.emit(SINGNAL_CHANGE_SETTING, item)

        if hasattr(item, 'flag') and item.flag == FLAG_RESULT_FILE_LIST:
            self.form.signal.emit(SINGNAL_SHOW_FILE_LIST, item)

        if hasattr(item, 'flag') and item.flag == FLAG_RESULT_FLOW_LIST:
            self.form.signal.emit(SINGNAL_FLOW_VIEW, item)

    def clear_all_select(self, node):
        if node is None:
            return
        for i in range(node.childCount()):
            item = node.child(i)
            item.setText(0, item.text(0).replace('[*]', ''))
            font = QFont()
            font.setBold(False)
            item.setFont(0, font)

    def add_setting(self, root):
        def add_set(name, flag, img):
            setting = QTreeWidgetItem(root)
            setting.flag = flag
            setting.setText(0, name)
            setting.setIcon(0, QIcon(QPixmap(img)))

        root.setExpanded(True)
        add_set('湍流模型', FLAG_TLMX, ':/db/B-shade抽样544.svg')
        add_set('多相流模型', FLAG_DXLMX, ':/db/B-shade抽样544.svg')
        add_set('介质特性设置', FLAG_JZTXSZ, ':/db/B-shade抽样544.svg')
        add_set('介质主相', FLAG_JZZX, ':/db/B-shade抽样544.svg')
        add_set('边界条件', FLAG_BJTJSZ, ':/db/B-shade抽样544.svg')
        add_set('自由面位置', FLAG_ZYMWZ, ':/db/B-shade抽样544.svg')
        add_set('动网格设置', FLAG_DWGSZ, ':/db/B-shade抽样544.svg')
        # add_set('计算参数设置', FLAG_JSCSSZ, ':/db/B-shade抽样544.svg')

    def add_tree(self):
        self.treeWidget_nav.setColumnCount(1)
        self.treeWidget_nav.header().setVisible(False)
        self.treeWidget_nav.itemClicked.connect(self.item_click)

        mesh = QTreeWidgetItem(self.treeWidget_nav)
        self.mesh = mesh
        mesh.flag = FLAG_MESH
        mesh.setText(0, f'网格导入')
        mesh.setIcon(0, QIcon(QPixmap(':/db/三维体分析692.svg')))
        mesh.setExpanded(True)

        setting = QTreeWidgetItem(self.treeWidget_nav)
        self.setting = setting
        setting.flag = FLAG_SETTING
        setting.setText(0, f'参数设置')
        setting.setIcon(0, QIcon(QPixmap(':/db/设置228.svg')))
        self.add_setting(setting)

        run = QTreeWidgetItem(self.treeWidget_nav)
        self.run = run
        run.flag = FLAG_RUN
        run.setText(0, f'计算')
        run.setIcon(0, QIcon(QPixmap(':/db/计算几何属性335.svg')))
        run.setExpanded(True)

        run2 = QTreeWidgetItem(run)
        run2.flag = FLAG_RUN_LIST
        run2.setText(0, f'开始计算')
        run2.setIcon(0, QIcon(QPixmap(':/db/计算几何属性335.svg')))

        result = QTreeWidgetItem(self.treeWidget_nav)
        self.result = result
        result.flag = FLAG_RESULT
        result.setText(0, f'结果查看')
        result.setIcon(0, QIcon(QPixmap(':/db/聚类分布138.svg')))
