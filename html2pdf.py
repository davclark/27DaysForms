#!/usr/bin/env python

from sys import argv, exit
from os import path

from PyQt5.QtCore import QUrl
# It'd be nice to just use QCoreApplication, but it appears that the QWebView
# needs to be in a GUI app
from PyQt5.QtWidgets import QApplication
from PyQt5.QtPrintSupport import QPrinter
# Note: QTextDocument only supports a subset of HTML
from PyQt5.QtWebKitWidgets import QWebView

app = QApplication(argv[:-2])

web = QWebView()
# This didn't work:
# with open(argv[1]) as html_file:
#     html_txt = html_file.read()
# web.setHtml(html_txt)

full_path = path.abspath(argv[1])
web.setUrl(QUrl.fromLocalFile(full_path))

# If you want to actually see these things
# web.show()

printer = QPrinter()
printer.setPageSize(QPrinter.Letter)
printer.setOutputFormat(QPrinter.PdfFormat)
basename, _ = path.splitext(path.basename(argv[1]))
print(basename)
printer.setOutputFileName('pdf_forms/' + basename + '.pdf')


def convertIt():
    web.print(printer)
    print("Pdf generated")
    QApplication.exit()

# May not be necessary with .setHtml, which is synchronous (I think)
web.loadFinished.connect(convertIt)

exit(app.exec())
