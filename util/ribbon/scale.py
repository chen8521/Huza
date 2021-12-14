from PyQt5.QtWidgets import QApplication


def gui_scale():
    screen = QApplication.screens()[0];
    dpi = screen.logicalDotsPerInch()
    return dpi / 96
