# -*- coding: utf-8 -*-

import time
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen


class SplashScreen(QSplashScreen):
    """Custom SplashScreen"""

    def __init__(self, picfile, extra):
        self.extra = extra
        if isinstance(picfile, QPixmap):
            pixmap = picfile
        else:
            pixmap = QPixmap(picfile)
        super(SplashScreen, self).__init__(pixmap)

        self.labelAlignment = int(Qt.AlignBottom | Qt.AlignHCenter | Qt.AlignAbsolute)
        self.show()
        QApplication.flush()

    def showMessage(self, msg):
        """Show the progress message on the splash image"""
        super(SplashScreen, self).showMessage(msg, self.labelAlignment, Qt.white)
        QApplication.processEvents()

    def clearMessage(self):
        """Clear message on the splash image"""
        super(SplashScreen, self).clearMessage()
        QApplication.processEvents()

    def setProgressText(self, percent, delay=0.1):
        """Show load percent in format 'Loading ... xx%' by showMessage method"""
        time.sleep(delay)  # 延时，给查看splashscreen更新数值
        self.showMessage(self.tr("Loading... {0}%").format(percent))

    def loadProgress(self):
        """Preimport modules to improve start speed
        Following modules are imported before splash:
        PyQt5, PyQt5.QtCore, PyQt5.QtGui, PyQt5.QtWidgets are imported before Splash.
        i18n is imported before Splash, for Splash using i18n.
        config is imported before i18n, for i18n using config.
        """
        if self.extra.debug:
            self.setProgressText(100)
            time.sleep(0.1)
            return
        self.setProgressText(0, 0)
        time.sleep(0.1)
        self.setProgressText(5)
        time.sleep(0.1)
        self.setProgressText(10)
        time.sleep(0.1)
        self.setProgressText(15)
        time.sleep(0.10)
        self.setProgressText(20)  # PyQt5, i18n are loaded, so before 20% do nothing
        time.sleep(0.10)
        self.setProgressText(40)
        time.sleep(0.10)
        self.setProgressText(60)
        time.sleep(0.10)
        self.setProgressText(80)
        time.sleep(0.10)
        self.setProgressText(100)
