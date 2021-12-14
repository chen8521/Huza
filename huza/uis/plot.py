# coding=utf-8
import re, os, time, codecs
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QTreeWidgetItem
from loguru import logger
from auto_ui.plot import Ui_Form
from util.constant import *


class Plot_Form(Ui_Form):

    def __init__(self, extra):
        self.extra = extra

    def setupUi(self, Form):
        self.form = Form
        super(Plot_Form, self).setupUi(Form)
        self.load()
        self.connect()

    def load(self):
        self.add_tree()

    def connect(self):
        self.treeWidget_nav.itemClicked.connect(self.item_click)

    def item_click(self, item):
        flag = item.flag
        if flag == 'quxian':
            self.form.signal.emit('quxian', 0)
        if flag == 'quxian2':
            self.form.signal.emit('quxian2', 0)

        if flag == 'sandian':
            self.form.signal.emit('sandian', 0)

        if flag == 'sample':
            self.form.signal.emit('sample', 0)

        if flag == 'quxian3':
            self.form.signal.emit('quxian3', 0)

        if flag == 'heatmap':
            self.form.signal.emit('heatmap', 0)
        if flag == 'yun':
            self.form.signal.emit('yun', 0)
        if flag == 'hexbin':
            self.form.signal.emit('hexbin', 0)
        if flag == 'times':
            self.form.signal.emit('times', 0)

        if flag == 'yun2':
            self.form.signal.emit('yun2', 0)

        if flag == 'td':
            self.form.signal.emit('td', 0)

        if flag == 'td2':
            self.form.signal.emit('td2', 0)
        if flag == 'movea':
            self.form.signal.emit('movea', 0)

        if flag =='readstl':
            self.form.signal.emit('readstl', 0)
        if flag =='readmesh':
            self.form.signal.emit('readmesh', 0)
    def add_tree(self):
        self.treeWidget_nav.setColumnCount(1)
        self.treeWidget_nav.header().setVisible(False)

        model = QTreeWidgetItem(self.treeWidget_nav)
        model.flag = 'quxian'
        model.setText(0, f'多曲线绘制')
        model.setIcon(0, QIcon(QPixmap(':/db/bim507.svg')))
        model.setExpanded(True)

        model = QTreeWidgetItem(self.treeWidget_nav)
        model.flag = 'quxian2'
        model.setText(0, f'多曲线绘制带图例')
        model.setIcon(0, QIcon(QPixmap(':/db/bim507.svg')))
        model.setExpanded(True)

        model = QTreeWidgetItem(self.treeWidget_nav)
        model.flag = 'sandian'
        model.setText(0, f'点与柱形图')
        model.setIcon(0, QIcon(QPixmap(':/db/bim507.svg')))
        model.setExpanded(True)

        model = QTreeWidgetItem(self.treeWidget_nav)
        model.flag = 'sample'
        model.setText(0, f'简单曲线')
        model.setIcon(0, QIcon(QPixmap(':/db/bim507.svg')))
        model.setExpanded(True)

        model = QTreeWidgetItem(self.treeWidget_nav)
        model.flag = 'quxian3'
        model.setText(0, f'带颜色曲线')
        model.setIcon(0, QIcon(QPixmap(':/db/bim507.svg')))
        model.setExpanded(True)

        model = QTreeWidgetItem(self.treeWidget_nav)
        model.flag = 'heatmap'
        model.setText(0, f'二维热力图')
        model.setIcon(0, QIcon(QPixmap(':/db/bim507.svg')))
        model.setExpanded(True)

        model = QTreeWidgetItem(self.treeWidget_nav)
        model.flag = 'yun'
        model.setText(0, f'二维云图1')
        model.setIcon(0, QIcon(QPixmap(':/db/bim507.svg')))
        model.setExpanded(True)

        model = QTreeWidgetItem(self.treeWidget_nav)
        model.flag = 'yun2'
        model.setText(0, f'二维云图2')
        model.setIcon(0, QIcon(QPixmap(':/db/bim507.svg')))
        model.setExpanded(True)

        model = QTreeWidgetItem(self.treeWidget_nav)
        model.flag = 'hexbin'
        model.setText(0, f'六边形热力图')
        model.setIcon(0, QIcon(QPixmap(':/db/bim507.svg')))
        model.setExpanded(True)

        model = QTreeWidgetItem(self.treeWidget_nav)
        model.flag = 'times'
        model.setText(0, f'热力图')
        model.setIcon(0, QIcon(QPixmap(':/db/bim507.svg')))
        model.setExpanded(True)

        model = QTreeWidgetItem(self.treeWidget_nav)
        model.flag = 'td'
        model.setText(0, f'三维云图')
        model.setIcon(0, QIcon(QPixmap(':/db/bim507.svg')))
        model.setExpanded(True)

        model = QTreeWidgetItem(self.treeWidget_nav)
        model.flag = 'td2'
        model.setText(0, f'三维中显示曲线')
        model.setIcon(0, QIcon(QPixmap(':/db/bim507.svg')))
        model.setExpanded(True)

        model = QTreeWidgetItem(self.treeWidget_nav)
        model.flag = 'movea'
        model.setText(0, f'点阵图带事件')
        model.setIcon(0, QIcon(QPixmap(':/db/bim507.svg')))
        model.setExpanded(True)

        model = QTreeWidgetItem(self.treeWidget_nav)
        model.flag = 'readstl'
        model.setText(0, f'读取STL模型')
        model.setIcon(0, QIcon(QPixmap(':/db/bim507.svg')))
        model.setExpanded(True)

        model = QTreeWidgetItem(self.treeWidget_nav)
        model.flag = 'readmesh'
        model.setText(0, f'读取网格数据')
        model.setIcon(0, QIcon(QPixmap(':/db/bim507.svg')))
        model.setExpanded(True)
