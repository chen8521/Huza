import os

from PyQt5.Qsci import QsciScintilla, QsciLexerBatch
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtWidgets import QHBoxLayout


def loadtext(self):
    sci_plot = QsciScintilla(self.form)
    sci_plot.setUtf8(True)
    sci_plot.setMarginWidth(0, 20)
    sci_plot.setMarginLineNumbers(0, True)
    sci_plot.setBraceMatching(QsciScintilla.StrictBraceMatch)
    sci_plot.setIndentationsUseTabs(True)
    sci_plot.setIndentationWidth(4)
    sci_plot.setTabIndents(True)
    sci_plot.setAutoIndent(True)
    sci_plot.setBackspaceUnindents(True)
    sci_plot.setTabWidth(4)
    sci_plot.setCaretLineVisible(True)
    sci_plot.setCaretLineBackgroundColor(QColor('#FFFFCD'))
    sci_plot.setIndentationGuides(True)
    sci_plot.setFolding(QsciScintilla.PlainFoldStyle)
    sci_plot.setMarginWidth(2, 12)
    sci_plot.markerDefine(QsciScintilla.Minus, QsciScintilla.SC_MARKNUM_FOLDEROPEN)
    sci_plot.markerDefine(QsciScintilla.Plus, QsciScintilla.SC_MARKNUM_FOLDER)
    sci_plot.markerDefine(QsciScintilla.Minus, QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
    sci_plot.markerDefine(QsciScintilla.Plus, QsciScintilla.SC_MARKNUM_FOLDEREND)
    sci_plot.setMarkerBackgroundColor(QColor("#FFFFFF"), QsciScintilla.SC_MARKNUM_FOLDEREND)
    sci_plot.setMarkerForegroundColor(QColor("#272727"), QsciScintilla.SC_MARKNUM_FOLDEREND)
    sci_plot.setMarkerBackgroundColor(QColor("#FFFFFF"), QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
    sci_plot.setMarkerForegroundColor(QColor("#272727"), QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
    sci_plot.setAutoCompletionSource(QsciScintilla.AcsAll)
    sci_plot.setAutoCompletionCaseSensitivity(True)
    sci_plot.setAutoCompletionReplaceWord(False)
    sci_plot.setAutoCompletionThreshold(1)
    sci_plot.setAutoCompletionUseSingle(QsciScintilla.AcusExplicit)
    lexer = QsciLexerBatch(sci_plot)
    sci_plot.setLexer(lexer)
    sci_plot.setScrollWidth(150)
    return sci_plot

def ShowText(self, args):
    filename = args
    text_w = self.loadtext()
    self.mains["panel"].ui().tabWidget.addTab(text_w, QIcon(QPixmap(':/db/任务管理199.svg')), filename)
    currentindex = self.mains["panel"].ui().tabWidget.count() - 1
    self.mains['panel'].ui().tabWidget.setCurrentIndex(currentindex)
    try:
        with open(os.path.join('projects',filename), 'r') as f:
            _str = f.read()
    except UnicodeDecodeError:
        _str = '文件不是ASCII文件格式'
    except Exception as e:
        _str = '未知错误'

    text_w.setText(_str)


