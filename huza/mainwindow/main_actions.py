from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
from loguru import logger

from huza.base.action import createAction


def addAction(self, name, text, tip=None, shortcut=None, icon=None, checkable=False, checked=False, slot=None,
              myactionname=None,
              enable=True):
    action = createAction(text, self.form, tip, shortcut, icon, checkable, checked, slot, myactionname, enable)
    if name in self.actions:
        logger.warning(f'Action[{name}]已经存在')
    self.actions[name] = action


