#!/usr/bin/env python3

from PyQt5.QtCore import QUrl

# It'd be nice to just use QCoreApplication, but the QWebPage
# needs to be in a GUI app
# We can probably run headless like so (commands are for debian-style distro)
# sudo apt-get install xvfb
# xvfb-run python render.py
from PyQt5.QtWidgets import QApplication
from PyQt5.QtPrintSupport import QPrinter

# This is an older implementation of the Qt web stack The more recent stack is
# the Qt WebEngine, but it's not as tightly packaged and apparently still
# doesn't compile on Windows:
# http://pyqt.sourceforge.net/Docs/PyQt5/introduction.html#module-PyQt5.QtWebEngineWidgets
# For now, this is probably best if it's working (it's deprecated...)
from PyQt5.QtWebKitWidgets import QWebPage


class PrintHTML(QWebPage):

    # Note sure if parent is necessary - got it from
    # https://gist.github.com/gciotta/7766803
    def __init__(self, infile, outfile):
        super(PrintHTML, self).__init__()
        url = QUrl.fromLocalFile(infile)
        self.mainFrame().setUrl(url)

        # If you want to actually see these things
        # self.show()

        self.printer = QPrinter()
        self.printer.setOutputFileName(outfile)
        self.printer.setOutputFormat(QPrinter.PdfFormat)
        self.printer.setPaperSize(QPrinter.Letter)

        self.loadFinished.connect(self.convertIt)

    def convertIt(self):
        self.mainFrame().print(self.printer)
        print('printed:', self.printer.outputFileName())
        QApplication.exit()


if __name__ == '__main__':
    from sys import argv, exit
    from os import path

    in_path = path.abspath(argv[1])
    basename, _ = path.splitext(path.basename(argv[1]))
    outfile = 'pdf_forms/' + basename + '.pdf'

    app = QApplication(argv[:-2])
    ph = PrintHTML(in_path, outfile)
    exit(app.exec())

