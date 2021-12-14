import os
import pickle

import numpy as np
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTreeWidgetItem, QHBoxLayout, QPushButton, QLabel, QMessageBox
from loguru import logger
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from toolz import partition_all

from uis.filelist import FileList_Form
from util.constant import *
from util.iconhand import IconHandle, IconHandle2
from util.navigationtool import MyNavigationToolbar2QT

from util.test_data import get_data2, get_data_3d

colors = ['#1f77b4',
          '#ff7f0e',
          '#2ca02c',
          '#d62728',
          '#9467bd',
          '#8c564b',
          '#e377c2',
          '#7f7f7f',
          '#bcbd22',
          '#17becf',
          '#1a55FF']

PNGS = ['0.0.png', '0.1.png', '0.2.png', '0.3.png', '0.4.png', '0.5.png', '0.6.png', '0.7.png', '0.8.png', '0.9.png',
        '1.0.png', '1.1.png', '1.2.png', '1.3.png', '1.4.png', '1.5.png', '1.6.png', '1.7.png', '1.8.png', '1.9.png',
        '2.0.png', '2.1.png', '2.2.png']

DATS = ['0.0.dat', '0.1.dat', '0.2.dat', '0.3.dat', '0.4.dat', '0.5.dat', '0.6.dat', '0.7.dat', '0.8.dat', '0.9.dat',
        '1.0.dat', '1.1.dat', '1.2.dat', '1.3.dat', '1.4.dat', '1.5.dat', '1.6.dat', '1.7.dat', '1.8.dat', '1.9.dat',
        '2.0.dat', '2.1.dat', '2.2.dat']


def get_position(num):
    dd = partition_all(84000 // len(PNGS), range(84000))
    for _i, i in enumerate(dd):
        if num in i:
            return _i
    return len(PNGS) - 1


def showfilelist(self, args):
    item = args
    if SINGNAL_SHOW_FILE_LIST in self.setups:
        self.setups[SINGNAL_SHOW_FILE_LIST].ui().adddata()
    self.setSetupView(SINGNAL_SHOW_FILE_LIST, item.text(0), FileList_Form)


def addpost(self):
    self.paras['szmn'].ui().result.takeChildren()

    mesh = QTreeWidgetItem(self.paras['szmn'].ui().result)
    mesh.flag = FLAG_RESULT_FILE_LIST
    mesh.setText(0, '结果文件查看')
    mesh.setIcon(0, QIcon(QPixmap(':/db/文件夹826.svg')))

    # mesh = QTreeWidgetItem(self.paras['szmn'].ui().result)
    # mesh.flag = FLAG_RESULT_FLOW_LIST
    # mesh.setText(0, '结果流场查看')
    # mesh.setIcon(0, QIcon(QPixmap(':/db/聚类分布138.svg')))
    self.paras['szmn'].ui().result.setExpanded(True)


def stop_calc(self, args):
    self.run_timmer.stop()
    self.setups[FLAG_RUN_LIST].ui().pushButton_run.setEnabled(True)
    self.setups[FLAG_RUN_LIST].ui().pushButton_stop.setEnabled(False)


def run_calc(self, args):
    if FLAG_DXLMX not in self.setups:
        QMessageBox.warning(self.form, "参数设置错误", f'请在多相流模型中设置网格维度!')
        return
    is2d = self.setups[FLAG_DXLMX].ui().radioButton_2d.isChecked()
    if os.path.exists('3d'):
        os.remove('3d')
    if os.path.exists('2d'):
        os.remove('2d')
    if is2d:
        self.run_calc_2d(args)
        with open('2d', 'w') as f:
            f.write('1')
    else:
        self.run_calc_3d(args)
        with open('3d', 'w') as f:
            f.write('1')


def run_calc_2d(self, args):
    speed = self.extra.speed if self.extra.debug else 1
    all_time = 10 * 60 * 60  # 确保10小时算完
    if self.extra.debug:
        all_time = all_time / speed

    def run_timmer_trigged():
        w = self.mains['panel'].ui().tab_chart.layout().itemAt(0).widget()
        label = self.mains['panel'].ui().tab_chart.layout().itemAt(1).widget()
        ax = w.myax
        canvas = w.mycanvas
        ax.cla()
        dt, _strpd = get_data2(self.slice_flag, all_time)

        dt_len = len(dt)
        png_index = get_position(dt_len)
        label.setPixmap(IconHandle().getIconByName(PNGS[png_index]))
        if self.last_2d_index != png_index:
            if os.path.exists('cache.dt'):
                path = 'cache.dt'
            elif os.path.exists('3rd/cache.dt'):
                path = '3rd/cache.dt'
            with open(path, 'rb') as f:
                alldata = pickle.load(f)
            _fdata = alldata[DATS[png_index]]
            with open(os.path.join('projects', DATS[png_index]), 'wb') as f:
                f.write(_fdata)
            self.last_2d_index = png_index

        if dt_len != self.last_lenth:
            self.last_lenth = dt_len
        self.docks["info"].widget().setText(_strpd)
        self.docks["info"].widget().verticalScrollBar().setValue(
            self.docks["info"].widget().verticalScrollBar().maximum())
        self.docks["info"].setVisible(True)
        if dt_len == 0:
            return
        if dt_len >= 84000:
            self.setups[FLAG_RUN_LIST].ui().pushButton_run.setEnabled(True)
            self.setups[FLAG_RUN_LIST].ui().pushButton_stop.setEnabled(False)
            ax.cla()
            canvas.draw()
            self.run_timmer.stop()
            self.addpost()

        dt_np = np.asarray(dt)
        x = dt_np[:, 0]
        plots = []
        plots_label = []
        y = dt_np[:, 1]
        l1, = ax.plot(x, y, label=f'', color=colors[0], linewidth='2.0')
        y = dt_np[:, 1]
        l2, = ax.plot(x, y, label=f'', color=colors[1], linewidth='2.0')
        y = dt_np[:, 3]
        l3, = ax.plot(x, y, label=f'', color=colors[2], linewidth='2.0')
        y = dt_np[:, 4]
        l4, = ax.plot(x, y, label=f'', color=colors[3], linewidth='2.0')
        y = dt_np[:, 5]
        l5, = ax.plot(x, y, label=f'', color=colors[4], linewidth='2.0')
        y = dt_np[:, 5]
        l6, = ax.plot(x, y, label=f'', color=colors[5], linewidth='2.0')
        y = dt_np[:, 7]
        l7, = ax.plot(x, y, label=f'', color=colors[6], linewidth='2.0')
        plots.append(l1)
        plots.append(l2)
        plots.append(l3)
        plots.append(l4)
        plots.append(l5)
        plots.append(l6)
        plots.append(l7)
        plots_label.append('continuity')
        plots_label.append('x-velocity')
        plots_label.append('y-velocity')
        plots_label.append('z-velocity')
        plots_label.append('k')
        plots_label.append('epsilon')
        plots_label.append('f-vapor')
        leg = ax.legend(plots, plots_label, loc='upper right', shadow=True)
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.get_legend().set_visible(True)
        ax.grid(True)
        canvas.draw()
        self.slice_flag += 1

    self.mains['panel'].ui().tabWidget.setCurrentIndex(0)
    if self.slice_flag == 0:
        w = self.drawplot()
        self.mains['panel'].ui().tab_chart.layout().addWidget(w)
        label = QLabel()
        label.setAlignment(Qt.AlignCenter)
        label.setMaximumHeight(300)
        self.mains['panel'].ui().tab_chart.layout().addWidget(label)
    self.setups[FLAG_RUN_LIST].ui().pushButton_run.setEnabled(False)
    self.setups[FLAG_RUN_LIST].ui().pushButton_stop.setEnabled(True)
    self.run_timmer = QTimer()
    self.run_timmer.timeout.connect(run_timmer_trigged)
    self.run_timmer.start(1000)


def run_calc_3d(self, args):
    speed = self.extra.speed if self.extra.debug else 1
    all_time = 10 * 60 * 60  # 确保10小时算完
    if self.extra.debug:
        all_time = all_time / speed

    def run_timmer_trigged():
        w = self.mains['panel'].ui().tab_chart.layout().itemAt(0).widget()
        label = self.mains['panel'].ui().tab_chart.layout().itemAt(1).widget()
        ax = w.myax
        canvas = w.mycanvas
        ax.cla()
        dt, _strpd = get_data_3d(self.slice_flag, all_time)
        dt_len = len(dt)
        if dt_len != self.last_lenth:
            self.last_lenth = dt_len
        self.docks["info"].widget().setText(_strpd)
        self.docks["info"].widget().verticalScrollBar().setValue(
            self.docks["info"].widget().verticalScrollBar().maximum())
        self.docks["info"].setVisible(True)
        if dt_len == 0:
            return
        if dt_len >= 1500:
            self.setups[FLAG_RUN_LIST].ui().pushButton_run.setEnabled(True)
            self.setups[FLAG_RUN_LIST].ui().pushButton_stop.setEnabled(False)
            ax.cla()
            canvas.draw()
            self.run_timmer.stop()
            self.addpost()

        dt_np = np.asarray(dt)
        x = dt_np[:, 0]
        plots = []
        plots_label = []
        y = dt_np[:, 1]
        l1, = ax.plot(x, y, label=f'', color=colors[0], linewidth='2.0')
        y = dt_np[:, 2]
        l2, = ax.plot(x, y, label=f'', color=colors[1], linewidth='2.0')
        y = dt_np[:, 3]
        l3, = ax.plot(x, y, label=f'', color=colors[2], linewidth='2.0')
        y = dt_np[:, 4]
        l4, = ax.plot(x, y, label=f'', color=colors[3], linewidth='2.0')
        y = dt_np[:, 5]
        l5, = ax.plot(x, y, label=f'', color=colors[4], linewidth='2.0')

        plots.append(l1)
        plots.append(l2)
        plots.append(l3)
        plots.append(l4)
        plots.append(l5)

        plots_label.append('log(rex)')
        plots_label.append('cl')
        plots_label.append('cd')
        plots_label.append('cy')
        plots_label.append('cmy')
        leg = ax.legend(plots, plots_label, loc='upper right', shadow=True)
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.get_legend().set_visible(True)
        ax.grid(True)
        canvas.draw()
        self.slice_flag += 1

    self.mains['panel'].ui().tabWidget.setCurrentIndex(0)
    if self.slice_flag == 0:
        w = self.drawplot()
        self.mains['panel'].ui().tab_chart.layout().addWidget(w)
        label = QLabel()
        label.setAlignment(Qt.AlignCenter)
        label.setPixmap(IconHandle2().getIconByName('3d.png'))
        label.setMaximumHeight(300)
        self.mains['panel'].ui().tab_chart.layout().addWidget(label)

    self.setups[FLAG_RUN_LIST].ui().pushButton_run.setEnabled(False)
    self.setups[FLAG_RUN_LIST].ui().pushButton_stop.setEnabled(True)
    self.run_timmer = QTimer()
    self.run_timmer.timeout.connect(run_timmer_trigged)
    self.run_timmer.start(1000)


def drawplot(self):
    contianerWidget = QWidget(self.form)
    lay = QVBoxLayout(self.form)
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)

    canvas = FigureCanvas(Figure(figsize=(5, 3)))
    self.canvas = canvas
    lay.addWidget(canvas)

    ctrol = MyNavigationToolbar2QT(canvas, self.form)
    canvas.figure.subplots_adjust(left=0.1, right=0.97, wspace=0.3, hspace=0.3)
    ax = canvas.figure.subplots()

    contianerWidget.myax = ax
    contianerWidget.myctrol = ctrol
    contianerWidget.mycanvas = canvas
    return contianerWidget
