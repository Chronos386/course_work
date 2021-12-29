from PyQt5 import QtCore, QtWidgets


class descrip(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(230, 250)
        MainWindow.setMinimumSize(QtCore.QSize(230, 250))
        MainWindow.setMaximumSize(QtCore.QSize(230, 250))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 210, 230))
        self.textBrowser.setMinimumSize(QtCore.QSize(210, 230))
        self.textBrowser.setMaximumSize(QtCore.QSize(210, 230))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Описание"))
