from huza.mainwindow import MainWindow_Form
from huza.util.mainui import get_dock_ui

from uis.bjtjsz import BJTJSZ_Form
from uis.dxlmx import DXLMX_Form
from uis.jztzsz import JZTZSZ_Form


def a(mainui: MainWindow_Form, arg):
    mainui.setDockView('jztzsz', 'JZTZSZ', 'setup', JZTZSZ_Form)


def b(mainui: MainWindow_Form, arg):
    mainui.setDockView('bjtjsz', 'BJTJSZ', 'setup', BJTJSZ_Form)


def c(mainui: MainWindow_Form, arg):
    mainui.setDockView('dxlmx', 'DXLMX', 'setup', DXLMX_Form)


def d(mainui: MainWindow_Form, arg):
    ui = get_dock_ui(mainui, 'setup', 'dxlmx')
    ui.checkBox_2.setText('fffffffffffffffffff')