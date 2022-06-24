default_style = """



QFrame{
    color: #222;
    background-color: #FDFDFD;/*不能设置为transparent*/
}

QMainWindow::separator{
    border: 1px solid #999999;
    border-style: outset;
    width: 4px;
    height: 4px;
}
QMainWindow::separator:hover{
    background: #8BF;
}
QSplitter::handle{
    border: 1px solid #999999;
    border-style: outset;
    width: 4px;
    height: 4px;
}

QSplitter::handle:hover{/*splitter->handle(1)->setAttribute(Qt::WA_Hover, true);才生效*/
    border-color: #EA2;
}
QSplitter::handle:pressed{
    border-color: #59F;
}
QSizeGrip{
    background-color: none;
}

/* =============================================== */
/* DockWidget                                       */
/* =============================================== */
QDockWidget, QDockWidget > QWidget/*not work*/
{
    border-color: #999999;/*qt bug*/
    background: transparent;
}
QDockWidget::title {
    border-bottom: 1px solid #999999;
    border-style: inset;
    text-align: left; /* align the text to the left */
    padding: 6px;
}

/* =============================================== */
/* Label                                           */
/* =============================================== */
QLabel {
    background: transparent;
    border: 1px solid transparent;
    padding: 1px;

}


/* A QLabel is a QFrame ... */
/* A QToolTip is a QLabel ... */
QToolTip {
    border: 1px solid #999999;
    padding: 5px;
    border-radius: 3px;
    opacity:210;
}

/* =============================================== */
/* TextBox                                         */
/* =============================================== */
QLineEdit {
    background: #FCFCFC;/*不建议设为透明，否则table编辑时会字显示*/
    selection-background-color: #8BF;
    border: 1px solid #999999;
    border-radius: 2px;
    border-style: inset;
    padding: 0 1px;

}

QLineEdit:hover{
    border-color: #8BF;
}
QLineEdit:focus{
    border-color: #EA2;
}
/*QLineEdit[readOnly="true"] { color: gray }*/
QLineEdit[echoMode="2"]{
    lineedit-password-character: 9679;/*字符的ascii码35 88等 */
}

QLineEdit:read-only {
     color: #353535;
    background: lightgray;
}

QLineEdit:disabled{
    color: #555555;
    background: lightgray;
}

QTextEdit{
    selection-background-color:#8BF;
    border: 1px solid #999999;
    border-style: inset;
}
QTextEdit:hover{
    border-color: #8BF;
}
QTextEdit:focus{
    border-color: #EA2;
}
/* =============================================== */
/* Button                                          */
/* =============================================== */
QPushButton {
    border: 1px solid #999999;
    border-radius: 2px;
    /*background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, 
        stop: 0 #EEEEEF, stop: 0.05 #DADADF,stop: 0.5 #DADADF, 
        stop: 0.9 #EEEEEF, stop: 1 #EEEEEF);*/
    padding: 1px 4px;
    min-width: 30px;
    min-height: 16px;
}

QPushButton:hover{
    background-color: #8BF;
    border-color: #59F;
}

QPushButton:pressed
{
    border-width: 1px;      
    background-color: #59F;
    border-color: #999999;
}

QPushButton:focus, QPushButton:default {
    border-color: #EA2; /* make the default button prominent */
}


QToolButton,QToolButton:unchecked { /* ToolBar里的按钮和带下拉菜单的按钮 */
    border: 1px solid transparent;
    border-radius: 3px;
    background-color: transparent;
    margin: 1px;
}
QToolButton:checked{
    background-color: #8BF;
    border-color: #59F;
}
QToolButton:hover{
    background-color: #8BF;
    border-color: #59F;
}

QToolButton:pressed,QToolButton:checked:hover{
    background-color: #59F;
    border-color: #EA2;
}
QToolButton:checked:pressed{
    background-color: #8BF;
}

/* only for MenuButtonPopup */
QToolButton[popupMode="1"]{
    padding-left: 1px;
    padding-right: 15px; /* make way for the popup button */
    border: 1px solid #999999;
    min-height: 15px;
    /*background: qlineargradient(x1:0, y1:0 ,x2:0, y2:1
        stop: 0 #EEEEEF, stop: 0.05 #DADADF, stop: 0.5 #DADADF
        stop: 0.95 #EEEEEF stop: 1#EEEEEF)*/
}
QToolButton[popupMode="1"]:hover{
    background-color: #8BF;
    border-color: #59F;
}
QToolButton[popupMode="1"]:pressed{
    border-width: 1px;
    background-color: #59F;
    border-color: #999999;
}
QToolButton::menu-button {
    border: 1px solid #999999;
    border-top-right-radius: 2px;
    border-bottom-right-radius: 2px;
    width: 16px;
}

/* =============================================== */
/* Slider ProgressBar                              */
/* =============================================== */
QProgressBar {
    border: 1px solid #999999;
    border-radius: 4px;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #EA2;
    width: 4px;
    margin: 1px;
}

QSlider{
    border: 1px solid transparent;
}
QSlider::groove{
    border: 1px solid #999999;
    background: #FDFDFD;
}
QSlider::handle {/*设置中间的那个滑动的键*/                           
    border: 1px solid #999999;
    background: #8BF;
}
QSlider::groove:horizontal {
    height: 3px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */
    left:5px; right: 5px;
}
QSlider::groove:vertical{
    width: 3px;
    top: 5px; bottom: 5px;
}
QSlider::handle:horizontal{
    width: 6px;
    margin: -7px; /* height */
}
QSlider::handle:vertical{
    height: 6px;
    margin: -7px; /* height */
}
QSlider::add-page{/*还没有滑上去的地方*/
    border: 1px solid #999999;
    background:#EEEEEF;
}
QSlider::sub-page{/*已经划过的从地方*/                            
    background: #EA2;
}

/* =============================================== */
/* GroupBox                                        */
/* =============================================== */
QGroupBox {
    background-color: #F0F0F0;
    border: 1px solid #999999;
    border-radius: 4px;
    margin-top: 0.5em;
    color: #222;
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 1em;
    background-color: #F0F0F0;
}

/* =============================================== */
/* QStackedWidget                                        */
/* =============================================== */
QStackedWidget {
    background-color: #F0F0F0;
    color: #222;
}



"""