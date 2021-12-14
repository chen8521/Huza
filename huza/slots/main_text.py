import codecs
import os
import re

import PyQt5
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QMessageBox, QVBoxLayout
from loguru import logger


def setText(self, args):
    if len(args) == 1:
        filename = args[0]
        scrolltoend = False
        readonly = True
    elif len(args) == 2:
        filename = args[0]
        scrolltoend = args[1]
        readonly = True
    elif len(args) == 3:
        filename = args[0]
        scrolltoend = args[1]
        readonly = args[2]
    if isinstance(args, str):
        filename = args
        scrolltoend = False
        readonly = True
    filepath = os.path.join(self.extra.project, filename)
    if not os.path.exists(filepath):
        QMessageBox.warning(self.form, "打开失败", f'文件[{filename}]不存在')
        return
    try:
        with open(filepath, 'r') as f:
            fstr = f.read()
    except Exception as e:
        logger.error(e)
        return

    self.setDockName('main', f'文本查看 [{filename}] 只读')
    contianerWidget = QWidget()
    if re.match('^\d+-\d+-\d+\.fit$',filename):
        contianerWidget.setToolTip("""当前点1	总点数Nt	该点样本数N
Y1拟合结果	Y2拟合结果	Yn拟合结果	Y1样本误差	Y2样本误差	Yn样本误差
*			*				*			*			*			*
*			*				*			*			*			*（重复N行）

当前点2	总点数Nt	该点样本数N 
Y1拟合结果	Y2拟合结果	Yn拟合结果	Y1样本误差	Y2样本误差	Yn样本误差
*			*				*			*			*			*
*			*				*			*			*			*（重复N行）""")
    elif re.match('^\d+-\d+-\d+\.poly$',filename):
        contianerWidget.setToolTip("""1    1   1  a1  k11  k12 …… k1m  (第1个网格点的第1个输出，重复n次)
1    1   2  a2  k21  k22 …… k2m 
1    1   N  aN  kN1  kN2 …… kNm  (重复N行)
1    2   1  a1  k11  k12 …… k1m  (第1个网格点的第2个输出，重复n次)
1    2   2  a2  k21  k22 …… k2m
1    2   N  aN  kN1  kN2 …… kNm (重复N行)
   ……                      (第1个网格点的第n个输出，重复n次)
                                       （重复Ntot个网格点）""")
    lay = QVBoxLayout()
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)
    textEdit = QsciScintilla(contianerWidget)
    textEdit.setUtf8(True)
    textEdit.setMarginWidth(0, 50)
    textEdit.setMarginLineNumbers(0, True)
    textEdit.setBraceMatching(QsciScintilla.StrictBraceMatch)
    textEdit.setIndentationsUseTabs(True)
    textEdit.setIndentationWidth(4)
    textEdit.setTabIndents(True)
    textEdit.setAutoIndent(True)
    textEdit.setBackspaceUnindents(True)
    textEdit.setTabWidth(4)
    textEdit.setCaretLineVisible(True)
    textEdit.setCaretLineBackgroundColor(QColor('#FFFFCD'))
    textEdit.setIndentationGuides(True)
    textEdit.setFolding(QsciScintilla.PlainFoldStyle)
    textEdit.setMarginWidth(2, 12)
    textEdit.markerDefine(QsciScintilla.Minus, QsciScintilla.SC_MARKNUM_FOLDEROPEN)
    textEdit.markerDefine(QsciScintilla.Plus, QsciScintilla.SC_MARKNUM_FOLDER)
    textEdit.markerDefine(QsciScintilla.Minus, QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
    textEdit.markerDefine(QsciScintilla.Plus, QsciScintilla.SC_MARKNUM_FOLDEREND)
    textEdit.setMarkerBackgroundColor(QColor("#FFFFFF"), QsciScintilla.SC_MARKNUM_FOLDEREND)
    textEdit.setMarkerForegroundColor(QColor("#272727"), QsciScintilla.SC_MARKNUM_FOLDEREND)
    textEdit.setMarkerBackgroundColor(QColor("#FFFFFF"), QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
    textEdit.setMarkerForegroundColor(QColor("#272727"), QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
    textEdit.SendScintilla(PyQt5.Qsci.QsciScintilla.SCI_SETTABWIDTH, 20)

    textEdit.setAutoCompletionSource(QsciScintilla.AcsAll)
    textEdit.setAutoCompletionCaseSensitivity(True)
    textEdit.setAutoCompletionReplaceWord(False)
    textEdit.setAutoCompletionThreshold(1)
    textEdit.setAutoCompletionUseSingle(QsciScintilla.AcusExplicit)
    self.lexer = QsciLexerMatlab(textEdit)
    textEdit.setLexer(self.lexer)
    textEdit.setText(fstr)
    textEdit.setScrollWidth(150)
    textEdit.setReadOnly(readonly)

    if scrolltoend:
        line = textEdit.SendScintilla(PyQt5.Qsci.QsciScintilla.SCI_GETLINECOUNT)
        textEdit.SendScintilla(PyQt5.Qsci.QsciScintilla.SCI_GOTOLINE, line)

    lay.addWidget(textEdit)
    self.docks["main"].setWidget(contianerWidget)
    self.setChartAction()


def setText2(self, args):
    if isinstance(args, str):
        filename = args
        scrolltoend = False
        readonly = True
    else:
        return
    filepath = filename
    if not os.path.exists(filepath):
        QMessageBox.warning(self.form, "打开失败", f'文件[{filename}]不存在')
        return
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            fstr = f.read()
    except Exception as e:
        logger.error(e)
        return

    self.setDockName('main', f'文本查看 [{filename}] 只读')
    contianerWidget = QWidget()
    lay = QVBoxLayout()
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)
    textEdit = QsciScintilla(contianerWidget)
    textEdit.setUtf8(True)
    textEdit.setMarginWidth(0, 50)
    textEdit.setMarginLineNumbers(0, True)
    textEdit.setBraceMatching(QsciScintilla.StrictBraceMatch)
    textEdit.setIndentationsUseTabs(True)
    textEdit.setIndentationWidth(4)
    textEdit.setTabIndents(True)
    textEdit.setAutoIndent(True)
    textEdit.setBackspaceUnindents(True)
    textEdit.setTabWidth(4)
    textEdit.setCaretLineVisible(True)
    textEdit.setCaretLineBackgroundColor(QColor('#FFFFCD'))
    textEdit.setIndentationGuides(True)
    textEdit.setFolding(QsciScintilla.PlainFoldStyle)
    textEdit.setMarginWidth(2, 12)
    textEdit.markerDefine(QsciScintilla.Minus, QsciScintilla.SC_MARKNUM_FOLDEROPEN)
    textEdit.markerDefine(QsciScintilla.Plus, QsciScintilla.SC_MARKNUM_FOLDER)
    textEdit.markerDefine(QsciScintilla.Minus, QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
    textEdit.markerDefine(QsciScintilla.Plus, QsciScintilla.SC_MARKNUM_FOLDEREND)
    textEdit.setMarkerBackgroundColor(QColor("#FFFFFF"), QsciScintilla.SC_MARKNUM_FOLDEREND)
    textEdit.setMarkerForegroundColor(QColor("#272727"), QsciScintilla.SC_MARKNUM_FOLDEREND)
    textEdit.setMarkerBackgroundColor(QColor("#FFFFFF"), QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
    textEdit.setMarkerForegroundColor(QColor("#272727"), QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
    textEdit.SendScintilla(PyQt5.Qsci.QsciScintilla.SCI_SETTABWIDTH, 20)

    textEdit.setAutoCompletionSource(QsciScintilla.AcsAll)
    textEdit.setAutoCompletionCaseSensitivity(True)
    textEdit.setAutoCompletionReplaceWord(False)
    textEdit.setAutoCompletionThreshold(1)
    textEdit.setAutoCompletionUseSingle(QsciScintilla.AcusExplicit)
    self.lexer = QsciLexerPython(textEdit)
    textEdit.setLexer(self.lexer)
    textEdit.setText(fstr)
    textEdit.setScrollWidth(150)
    textEdit.setReadOnly(readonly)

    if scrolltoend:
        line = textEdit.SendScintilla(PyQt5.Qsci.QsciScintilla.SCI_GETLINECOUNT)
        textEdit.SendScintilla(PyQt5.Qsci.QsciScintilla.SCI_GOTOLINE, line)

    lay.addWidget(textEdit)
    self.docks["main"].setWidget(contianerWidget)
    self.setChartAction()

