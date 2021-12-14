from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from util.version import VERSION


def addWelcome(self):
    self.setDockName('main', f'欢迎页面')

    welcomeWidget = QWidget()
    lay = QVBoxLayout()
    lay.setContentsMargins(0, 0, 0, 0)
    welcomeWidget.setLayout(lay)
    label = QLabel(welcomeWidget)
    label.setText(f'水下发射高精度数值模拟软件 Ver-{VERSION}')
    label.setFont(QFont('Microsoft YaHei', 30, 50))
    label.setAlignment(QtCore.Qt.AlignCenter)
    lay.addWidget(label)
    self.docks["main"].setWidget(welcomeWidget)