from huza.base.mainwindow_run import MainWindowRun
from uis.navigate import NaviGate_Form
from uis.showicon import ShowIcon_Form


def exit_connect(self):
    exit = self.get_action('exit')
    exit.triggered.connect(self.mainwindow.close)


def show_connect(self):
    showpara = self.get_action('showpara')
    para_dock = self.get_dock('para')
    para_dock.visibilityChanged.connect(showpara.setChecked)

    def showpara_tri(show):
        para_dock.setVisible(show)

    showpara.triggered.connect(showpara_tri)

    showinfo = self.get_action('showinfo')
    info_dock = self.get_dock('info')
    info_dock.visibilityChanged.connect(showinfo.setChecked)
    def showinfo_tri(show):
        info_dock.setVisible(show)
    showinfo.triggered.connect(showinfo_tri)


def t1_connect(self):
    t1 = self.get_action('t1')

    def navi():
        self.set_dock_view('navi', '功能', 'para', NaviGate_Form)

    t1.triggered.connect(navi)


def showicon_connect(self):
    showicon = self.get_action('showicon')

    def showicon_tri():
        self.set_dock_view('icon', '图标', 'main', ShowIcon_Form)

    showicon.triggered.connect(showicon_tri)


def init_connect(self: MainWindowRun):
    exit_connect(self)
    show_connect(self)
    t1_connect(self)
    showicon_connect(self)
