from PyQt5.QtWidgets import QAction


def createAction(text, parent, tip=None, shortcut=None, icon=None, checkable=False, checked=False, slot=None,
                 myactionname=None,
                 enable=True):
    action = QAction(text, parent)
    if icon is not None:
        action.setIcon(icon)
    if shortcut is not None:
        action.setShortcut(shortcut)
    if tip is not None:
        tip = tip
        action.setToolTip(tip)
        action.setStatusTip(tip)
    if checkable:
        action.setCheckable(True)
        action.setChecked(checked)
    if slot is not None:
        action.triggered.connect(slot)
    if myactionname is not None:
        action.myactionname = myactionname
    action.setEnabled(enable)
    return action
