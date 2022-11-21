import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from tkinter import Tk, messagebox

from loguru import logger


class MyQmainWindow(QMainWindow):
    signal = pyqtSignal(object, object)

    def _set_close_info(self, mainform):
        self.mainform = mainform

    def closeEvent(self, QCloseEvent):
        if not self.mainform.extra.debug:
            if hasattr(self.mainform, '_close_process') and (self.mainform._close_loc & 0b100) >> 2:
                self.mainform._close_process()
            title = '关闭确认' if not hasattr(self.mainform, '_close_title') else self.mainform._close_title
            msg = '是否关闭软件？' if not hasattr(self.mainform, '_close_msg') else self.mainform._close_msg
            r = QMessageBox.question(self, title, msg,
                                     QMessageBox.Yes | QMessageBox.No)
            if r == QMessageBox.Yes:
                event = super(MyQmainWindow, self).closeEvent(QCloseEvent)
                if hasattr(self.mainform, '_close_process') and (self.mainform._close_loc & 0b010) >> 1:
                    self.mainform._close_process()
                return event
            else:
                if hasattr(self.mainform, '_close_process') and (self.mainform._close_loc & 0b001) >> 0:
                    self.mainform._close_process()
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
