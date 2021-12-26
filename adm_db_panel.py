from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from all_models import *


class Ui_MainWindow(object):
    def __init__(self):
        self.prov = 0;
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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_func()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Выберите таблицу из списка"))
        self.groupBox.setTitle(_translate("MainWindow", "Изменение таблицы"))
        self.label_3.setText(_translate("MainWindow", "Выберите столбец из таблицы"))
        self.label_4.setText(_translate("MainWindow", "Выберите строку из таблицы"))
        self.label_5.setText(_translate("MainWindow", "Выберите как изменить табл."))
        self.pushButton_2.setText(_translate("MainWindow", "Изменить таблицу"))
        self.pushButton_3.setText(_translate("MainWindow", "Подтвердить изменение"))
        self.pushButton_4.setText(_translate("MainWindow", "Отменить изменение"))
        self.label_2.setText(_translate("MainWindow", "Поле ввода"))
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

    def add_func(self):
        self.pushButton.clicked.connect(lambda: self.show_table())
        self.pushButton_2.clicked.connect(lambda: self.change_table())
        self.pushButton_3.clicked.connect(lambda: self.confirm_change())
        self.pushButton_4.clicked.connect(lambda: self.undo_change())

    def show_table(self):
        self.comboBox_2.clear()
        self.comboBox_3.clear()
        self.listView.clearSelection()
        result = self.comboBox.currentText()
        line = 0
        collums = []
        if result == "Типы оружия":
            line = session.query(weapon_types).count()
            self.listView.setColumnCount(2)
            self.qTable = session.query(weapon_types).all()
            collums = ['id', 'name']
            self.listView.setHorizontalHeaderLabels(["ID", "Название"])
        if result == "Типы брони":
            line = session.query(armor_types).count()
            self.listView.setColumnCount(2)
            self.qTable = session.query(armor_types).all()
            collums = ['id', 'name']
            self.listView.setHorizontalHeaderLabels(["ID", "Название"])
        if result == "Статусы пользователя":
            line = session.query(user_status).count()
            self.listView.setColumnCount(2)
            self.qTable = session.query(user_status).all()
            collums = ['id', 'status']
            self.listView.setHorizontalHeaderLabels(["ID", "Статус"])
        if result == "Описания":
            line = session.query(descriptions).count()
            self.listView.setColumnCount(2)
            self.qTable = session.query(descriptions).all()
            collums = ['id', 'field']
            self.listView.setHorizontalHeaderLabels(["ID", "Описание"])
        if result == "Расы":
            line = session.query(Races).count()
            self.listView.setColumnCount(7)
            self.qTable = session.query(Races).all()
            collums = ['id', 'name', 'incr_char', 'worldview', 'size', 'speed', 'descr_id']
            self.listView.setHorizontalHeaderLabels(
                ["ID", "Название", "Повышение характеристик", "Мировозрение", "Размер", "Скорость", "ID описания"])
        if result == "Разновидности рас":
            line = 14#session.query(var_races).count()
            self.listView.setColumnCount(6)
            self.qTable = session.query(var_races).all()
            collums = ['id', 'name', 'incr_char', 'add_feat', 'rac_id', 'descr_id']
            self.listView.setHorizontalHeaderLabels(["ID", "Название", "Повышение характеристик", "Доп. способность", "ID расы", "ID описания"])
        if result == "Аккаунты":
            line = session.query(Accounts).count()
            self.listView.setColumnCount(4)
            self.qTable = session.query(Accounts).all()
            collums = ['id', 'login', 'password', 'stat_id']
            self.listView.setHorizontalHeaderLabels(["ID", "Логин", "Пароль", "ID статуса"])
        if result == "Классы":
            line = session.query(Classes).count()
            self.listView.setColumnCount(5)
            self.qTable = session.query(Classes).all()
            collums = ['id', 'name', 'master_bonus', 'numb_av_spells', 'descr_id']
            self.listView.setHorizontalHeaderLabels(["ID", "Название", "Бонус мастерства", "Кол-во доступных заклинаний", "ID описания"])
        if result == "Оружие":
            line = session.query(Weapon).count()
            self.listView.setColumnCount(6)
            self.qTable = session.query(Weapon).all()
            collums = ['id', 'name', 'price', 'damage', 'weight', 'weap_t_id']
            self.listView.setHorizontalHeaderLabels(["ID", "Название", "Цена", "Урон", "Вес", "ID типа"])
        if result == "Броня":
            line = session.query(Armor).count()
            self.listView.setColumnCount(6)
            self.qTable = session.query(Armor).all()
            collums = ['id', 'name', 'price', 'steal_hindr', 'weight', 'arm_t_id']
            self.listView.setHorizontalHeaderLabels(["ID", "Название", "Цена", "Громкий", "Вес", "ID типа"])
        if result == "Таблица заклинаний":
            line = session.query(Spell_table).count()
            self.listView.setColumnCount(6)
            self.qTable = session.query(Spell_table).all()
            collums = ['id', 'name', 'level', 'distance', 'duration', 'descr_id']
            self.listView.setHorizontalHeaderLabels(["ID", "Название", "Уровень", "Дистанция", "Длительность", "ID описания"])
        if result == "Связи типов оружия и классов":
            line = 21#session.query(Relat_table_t_weap_t_cl).count()
            self.listView.setColumnCount(3)
            self.qTable = session.query(Relat_table_t_weap_t_cl).all()
            collums = ['id', 'weap_t_id', 'class_id']
            self.listView.setHorizontalHeaderLabels(["ID", "ID типа оружия", "ID класса"])
        if result == "Связи типов доспехов и классов":
            line = 25#session.query(Relat_table_t_arm_t_cl).count()
            self.listView.setColumnCount(3)
            self.qTable = session.query(Relat_table_t_arm_t_cl).all()
            collums = ['id', 'arm_t_id', 'class_id']
            self.listView.setHorizontalHeaderLabels(["ID", "ID типа брони", "ID класса"])
        if result == "Связи заклинаний и классов":
            line = 28#session.query(Relat_table_t_spell_cl).count()
            self.listView.setColumnCount(3)
            self.qTable = session.query(Relat_table_t_spell_cl).all()
            collums = ['id', 'spell_id', 'class_id']
            self.listView.setHorizontalHeaderLabels(["ID", "ID заклинания", "ID класса"])
        if result == "Персонаж":
            line = session.query(Character).count()
            self.listView.setColumnCount(13)
            self.qTable = session.query(Character).all()
            collums = ['id', 'name', 'power', 'agility', 'body_type', 'intellect', 'wisdom', 'charisma', 'acc_id', 'var_races_id', 'class_id', 'weap_id', 'arm_id']
            self.listView.setHorizontalHeaderLabels(["ID", "Имя", "Сила", "Ловкость", "Телосложение", "Интеллект", "Мудрость", "Харизма", "ID аккаунта", "ID разновидности расы", "ID класса", "ID оружия", "ID брони"])

        self.listView.setRowCount(line)
        for i in collums:
            if i != 'id':
                self.comboBox_2.addItem(i)
        for i in range(line):
            self.comboBox_3.addItem(str(i + 1))
        for row, form in enumerate(self.qTable):
            col = 0
            for c in collums:
                for k, v in vars(form).items():
                    if c == k:
                        self.listView.setItem(row, col, QTableWidgetItem(str(v)))
                        col += 1
        self.listView.setStyleSheet("selection-color: rgb(255, 0, 127);\n"
                                    "selection-background-color: rgb(85, 255, 127);")
        self.listView.resizeColumnsToContents()

    def change_table(self):
        self.statusbar.clearMessage()
        if self.prov == 0:
            self.transaction = conn.begin()
            self.prov = 1
        result = self.comboBox.currentText()
        change = self.comboBox_2.currentText()
        stlb = int(self.comboBox_3.currentText())
        table = Weapon
        act = delete(Weapon).where(Weapon.id == 1)
        if result == "Типы оружия":
            table = weapon_types
        if result == "Типы брони":
            table = armor_types
        if result == "Статусы пользователя":
            table = user_status
        if result == "Описания":
            table = descriptions
        if result == "Расы":
            table = Races
        if result == "Разновидности рас":
            table = var_races
        if result == "Аккаунты":
            table = Accounts
        if result == "Классы":
            table = Classes
        if result == "Оружие":
            table = Weapon
        if result == "Броня":
            table = Armor
        if result == "Таблица заклинаний":
            table = Spell_table
        if result == "Связи типов оружия и классов":
            table = Relat_table_t_weap_t_cl
        if result == "Связи типов доспехов и классов":
            table = Relat_table_t_arm_t_cl
        if result == "Связи заклинаний и классов":
            table = Relat_table_t_spell_cl
        if result == "Персонаж":
            table = Character
        act = delete(table).where(table.id == 1)
        if change == "Добавить строку":
            act = insert(table).values(name='username', fullname='Full Username')
        if change == "Удалить строку":
            act = delete(table).where(table.id == stlb)

        conn.execute(act)
        self.show_table()

    def confirm_change(self):
        if self.prov != 0:
            self.transaction.commit()
            self.prov = 0
            self.show_table()
        else:
            self.statusbar.showMessage("Сначала внесите изменение в таблицу")

    def undo_change(self):
        if self.prov != 0:
            self.transaction.rollback()
            self.prov = 0
            self.show_table()
        else:
            self.statusbar.showMessage("Сначала внесите изменение в таблицу")
