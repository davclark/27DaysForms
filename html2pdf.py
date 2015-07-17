#!/usr/bin/env python

from sys import argv, exit
from os import path

from PyQt4.QtCore import QObject, SIGNAL, QUrl
from PyQt4.QtGui import QApplication, QPrinter
# Note: QTextDocument only supports a subset of HTML
from PyQt4.QtWebKit import QWebView

app = QApplication(argv[:-2])

web = QWebView()
# with open(argv[1]) as html_file:
#     html_txt = html_file.read()
# web.setHtml(html_txt)
full_path = path.abspath(argv[1])
web.setUrl(QUrl.fromLocalFile(full_path))
# web.show()

printer = QPrinter()
printer.setPageSize(QPrinter.Letter)
printer.setOutputFormat(QPrinter.PdfFormat)
basename, _ = path.splitext(argv[1])
printer.setOutputFileName(basename + '.pdf')

def convertIt():
    web.print_(printer)
    print("Pdf generated")
    QApplication.exit()

# .setHtml is synchronous (I think)
QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)

exit(app.exec_())
