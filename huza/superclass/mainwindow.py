import sys

from PyQt5.QtWidgets import QMessageBox, QMainWindow
from tkinter import Tk, messagebox

from loguru import logger


class MyQmainWindow(QMainWindow):
    def _set_close_waring(self, extra):
        self.extra = extra

    def closeEvent(self, QCloseEvent):
        if hasattr(self, 'closeprocess'):
            self.closeprocess()
        if not self.extra.debug:
            r = QMessageBox.question(self, '关闭确认', '是否关闭软件？',
                                     QMessageBox.Yes | QMessageBox.No)
            if r == QMessageBox.Yes:
                return super(MyQmainWindow, self).closeEvent(QCloseEvent)
            else:
                QCloseEvent.ignore()


def except_hook(exc_type, exception, traceback):
    """"""
    msg = ' Traceback (most recent call last):\n'
    while traceback:
        filename = traceback.tb_frame.f_code.co_filename
        name = traceback.tb_frame.f_code.co_name
        lineno = traceback.tb_lineno
        msg += '   File "%.500s", line %d, in %.500s\n' % (filename, lineno, name)
        traceback = traceback.tb_next
    msg += ' %s: %s\n' % (exc_type.__name__, exception)

    logger.exception(exception)
    root = Tk()
    root.withdraw()
    txt = messagebox.showinfo("错误", msg)
    root.destroy()
    sys.__excepthook__(exc_type, exception, traceback)
