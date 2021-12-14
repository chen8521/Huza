import os

from PyQt5.QtWidgets import QMessageBox

from uis.navigate import Navigate_Form
from uis.plot import Plot_Form
from uis.plotflow import PlotFlow_Form
from matplotlib.backend_bases import _Mode

from util.myfigureoptions import edit_parameters


def solt_action_szmn(self):
    action = self.form.sender()
    self.setParaView(action, Navigate_Form)
    self.setMainView('panel','画布', PlotFlow_Form)
    self.actions["importmesh"].setEnabled(True)




def solt_action_help_version(self):
    if os.path.exists('3rd/release.txt'):
        self.setText2('3rd/release.txt')
    else:
        self.setText2('release.txt')


def solt_action_coordinate_legend(self):
    ischecked = self.actions["coordinate_legend"].isChecked()
    self.setLagendEnable(ischecked)


def solt_action_coordinate_zoom(self):
    ischecked = self.actions["coordinate_zoom"].isChecked()
    self.actions["coordinate_move"].setChecked(False)
    if ischecked:
        self.setChartMode(_Mode.ZOOM)
    else:
        self.setChartMode(_Mode.NONE)


def solt_action_gendemo(self):
    action = self.form.sender()
    self.setParaView(action, Plot_Form)


def solt_action_coordinate_move(self):
    ischecked = self.actions["coordinate_move"].isChecked()
    self.actions["coordinate_zoom"].setChecked(False)
    if ischecked:
        self.setChartMode(_Mode.PAN)
    else:
        self.setChartMode(_Mode.NONE)


def solt_action_coordinate_zoom_reset(self):
    self.setRest(None)
    self.setChartMode(_Mode.NONE)
    self.actions["coordinate_zoom"].setChecked(False)
    self.actions["coordinate_move"].setChecked(False)


def solt_action_coordinate_save(self):
    self.setSaveFigure(None)


def solt_action_help_doc(self):
    help_d = os.path.join('3rd', 'help.pdf')
    if os.path.exists(help_d):
        os.startfile(help_d)
    elif os.path.exists('help.pdf'):
        os.startfile('help.pdf')


def solt_action_help_about(self):
    aboutText = "<b><center>水下发射高精度数值模拟软件</center></b><br><br>"
    aboutText += self.tr(
        "    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX。<br><br>")
    aboutText += self.tr(
        "   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX<br>"
        "<br> 开发<br><br>")
    aboutText += "版权所有： XXXXXX"
    QMessageBox.about(self.form, "关于", aboutText)


def setChartAction(self):
    ischart = hasattr(self.docks['main'].widget(), 'myax')
    self.actions['coordinate_textedit'].setEnabled(ischart)
    self.actions['coordinate_legend'].setEnabled(ischart)
    self.actions['coordinate_set'].setEnabled(ischart)
    self.actions['coordinate_zoom'].setEnabled(ischart)
    self.actions['coordinate_zoom_reset'].setEnabled(ischart)
    self.actions['coordinate_move'].setEnabled(ischart)
    self.actions['coordinate_save'].setEnabled(ischart)
    # if hasattr(self.docks['main'].widget(), 'mytype'):
    #     mytype = self.docks['main'].widget().mytype
    #     # todo legend显示与隐藏控制
    #     # self.actions['coordinate_legend'].setChecked(para[mytype]['showlagend'])


def solt_action_coordinate_textedit(self):
    action = self.form.sender()
    return


def solt_action_coordinate_set(self):
    chartwidget = self.docks['main'].widget()
    if not hasattr(chartwidget, 'mycanvas'):
        return
    canvas = chartwidget.mycanvas
    index, data = edit_parameters(canvas, self.form)
    if data is None:
        return
    if not hasattr(chartwidget, 'mytype'):
        return
    mytype = chartwidget.mytype
