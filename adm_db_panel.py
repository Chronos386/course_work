from PyQt5 import QtCore, QtWidgets
import sys


class Ui_MainWindow:
    def __init__(self):
        self.action = None
        self.menu = None
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = None
        self.ui = None
        self.prov = 0
        self.textBrowser = None
        self.transaction = None
        self.label_2 = None
        self.qTable = None
        self.formLayout = None
        self.statusbar = None
        self.menubar = None
        self.pushButton = None
        self.verticalLayout_2 = None
        self.pushButton_4 = None
        self.pushButton_2 = None
        self.pushButton_3 = None
        self.comboBox_4 = None
        self.label_5 = None
        self.comboBox_3 = None
        self.label_4 = None
        self.comboBox_2 = None
        self.label_3 = None
        self.verticalLayout_4 = None
        self.groupBox = None
        self.comboBox = None
        self.label = None
        self.verticalLayout = None
        self.verticalLayout_3 = None
        self.listView = None
        self.horizontalLayout = None
        self.centralwidget = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(776, 634)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.listView = QtWidgets.QTableWidget(self.centralwidget)
        self.listView.setMinimumSize(QtCore.QSize(520, 0))
        self.listView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listView.setObjectName("listView")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.listView)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(195, 15))
        self.label.setMaximumSize(QtCore.QSize(195, 15))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(220, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(220, 30))
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(220, 290))
        self.groupBox.setMaximumSize(QtCore.QSize(220, 290))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMinimumSize(QtCore.QSize(195, 15))
        self.label_3.setMaximumSize(QtCore.QSize(195, 15))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_2.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_4.addWidget(self.comboBox_2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMinimumSize(QtCore.QSize(195, 15))
        self.label_4.setMaximumSize(QtCore.QSize(195, 15))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_3.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_4.addWidget(self.comboBox_3)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setMinimumSize(QtCore.QSize(195, 15))
        self.label_5.setMaximumSize(QtCore.QSize(195, 15))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_4.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_4.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout_4.addWidget(self.comboBox_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setMinimumSize(QtCore.QSize(207, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(207, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setMinimumSize(QtCore.QSize(207, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(207, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setMinimumSize(QtCore.QSize(207, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(207, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.textBrowser = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(210, 140))
        self.textBrowser.setMaximumSize(QtCore.QSize(210, 140))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(220, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(220, 30))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 776, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.add_func()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Окно управления Базой Данных"))
        self.label.setText(_translate("MainWindow", "Выберите таблицу из списка"))
        self.groupBox.setTitle(_translate("MainWindow", "Изменение таблицы"))
        self.label_3.setText(_translate("MainWindow", "Выберите столбец из таблицы"))
        self.label_4.setText(_translate("MainWindow", "Выберите строку из таблицы"))
        self.label_5.setText(_translate("MainWindow", "Выберите как изменить табл."))
        self.pushButton_2.setText(_translate("MainWindow", "Изменить таблицу"))
        self.pushButton_3.setText(_translate("MainWindow", "Подтвердить изменение"))
        self.pushButton_4.setText(_translate("MainWindow", "Отменить изменение"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.action.setText(_translate("MainWindow", "Назад"))
        self.label_2.setText(_translate("MainWindow", "Ввод переменных через \',\'"))
        self.pushButton.setText(_translate("MainWindow", "Вывести таблицу"))
        self.comboBox.addItem("Типы оружия")
        self.comboBox.addItem("Типы брони")
        self.comboBox.addItem("Статусы пользователя")
        self.comboBox.addItem("Описания")
        self.comboBox.addItem("Расы")
        self.comboBox.addItem("Разновидности рас")
        self.comboBox.addItem("Аккаунты")
        self.comboBox.addItem("Классы")
        self.comboBox.addItem("Оружие")
        self.comboBox.addItem("Броня")
        self.comboBox.addItem("Таблица заклинаний")
        self.comboBox.addItem("Связи типов оружия и классов")
        self.comboBox.addItem("Связи типов доспехов и классов")
        self.comboBox.addItem("Связи заклинаний и классов")
        self.comboBox.addItem("Персонаж")
        self.comboBox_4.addItem("Добавить строку")
        self.comboBox_4.addItem("Удалить строку")
        self.comboBox_4.addItem("Обновить элемент")
