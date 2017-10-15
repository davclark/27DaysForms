#!/usr/bin/env python3

from sys import argv, exit
from os import path

# It'd be nice to just use QCoreApplication, but the QWebPage
# needs to be in a GUI app
# We can probably run headless like so (commands are for debian-style distro)
# sudo apt-get install xvfb
# xvfb-run python render.py
from PyQt5.QtWidgets import QApplication
# I find it easier to work with QPrinter than a layout object
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtCore import QUrl
# We are now using the more recent stack, Qt WebEngine
from PyQt5.QtWebEngineWidgets import QWebEnginePage

# Get our paths sorted out
in_path = path.abspath(argv[1])
basename, _ = path.splitext(path.basename(argv[1]))
outfile = 'pdf_forms/' + basename + '.pdf'

# The below could be made into a class, but I am totally done messing with Qt for now...

# Fire up Qt
app = QApplication(argv)

# This doesn't open up a GUI on Windows at least
web = QWebEnginePage()
url = QUrl.fromLocalFile(in_path)
web.load(url)

printer = QPrinter()
printer.setPaperSize(QPrinter.Letter)
printer.setOutputFormat(QPrinter.PdfFormat)
printer.setOutputFileName(outfile)

def done(result):
    app.quit()

# We are being quite lazy here - referencing variables in the containing scope
def convertIt():
    web.print(printer, done)
    print('printed:', printer.outputFileName())
    # QApplication.exit()

# This sets up a chain of callbacks that should lead to a clean exit
web.loadFinished.connect(convertIt)

app.exec_()
