from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.QtWidgets import QTableWidgetItem
from all_models import *
from adm_db_panel import Ui_MainWindow
from login_panel import login_panell


class Admin_db_Panel(QMainWindow):
    def __init__(self, parent=None):
        super(Admin_db_Panel, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.show_table())
        self.ui.pushButton_2.clicked.connect(lambda: self.change_table())
        self.ui.pushButton_3.clicked.connect(lambda: self.confirm_change())
        self.ui.pushButton_4.clicked.connect(lambda: self.undo_change())
        self.ui.action.triggered.connect(lambda: self.exit_db_panel())

    def show_table(self):
        self.ui.comboBox_2.clear()
        self.ui.comboBox_3.clear()
        self.ui.listView.clearSelection()
        result = self.ui.comboBox.currentText()
        table = Weapon
        line = 0
        collums = []
        if result == "Типы оружия":
            table = weapon_types
            line = session.query(weapon_types).count()
            self.ui.listView.setColumnCount(2)
            self.ui.qTable = session.query(weapon_types).all()
            collums = ['id', 'name']
            self.ui.listView.setHorizontalHeaderLabels(["ID", "Название"])
        if result == "Типы брони":
            table = armor_types
            line = session.query(armor_types).count()
            self.ui.listView.setColumnCount(2)
            self.ui.qTable = session.query(armor_types).all()
            collums = ['id', 'name']
            self.ui.listView.setHorizontalHeaderLabels(["ID", "Название"])
        if result == "Статусы пользователя":
            table = user_status
            line = session.query(user_status).count()
            self.ui.listView.setColumnCount(2)
            self.ui.qTable = session.query(user_status).all()
            collums = ['id', 'status']
            self.ui.listView.setHorizontalHeaderLabels(["ID", "Статус"])
        if result == "Описания":
            table = descriptions
            line = session.query(descriptions).count()
            self.ui.listView.setColumnCount(2)
            self.ui.qTable = session.query(descriptions).all()
            collums = ['id', 'field']
            self.ui.listView.setHorizontalHeaderLabels(["ID", "Описание"])
        if result == "Расы":
            table = Races
            line = session.query(Races).count()
            self.ui.listView.setColumnCount(7)
            self.ui.qTable = session.query(Races).all()
            collums = ['id', 'name', 'incr_char', 'worldview', 'size', 'speed', 'descr_id']
            self.ui.listView.setHorizontalHeaderLabels(
                ["ID", "Название", "Повышение характеристик", "Мировозрение", "Размер", "Скорость", "ID описания"])
        if result == "Разновидности рас":
            table = var_races
            line = 14  # session.query(var_races).count()
            self.ui.listView.setColumnCount(6)
            self.ui.qTable = session.query(var_races).all()
            collums = ['id', 'name', 'incr_char', 'add_feat', 'rac_id', 'descr_id']
            self.ui.listView.setHorizontalHeaderLabels(
                ["ID", "Название", "Повышение характеристик", "Доп. способность", "ID расы", "ID описания"])
        if result == "Аккаунты":
            table = Accounts
            line = session.query(Accounts).count()
            self.ui.listView.setColumnCount(4)
            self.ui.qTable = session.query(Accounts).all()
            collums = ['id', 'login', 'password', 'stat_id']
            self.ui.listView.setHorizontalHeaderLabels(["ID", "Логин", "Пароль", "ID статуса"])
        if result == "Классы":
            table = Classes
            line = session.query(Classes).count()
            self.ui.listView.setColumnCount(5)
            self.ui.qTable = session.query(Classes).all()
            collums = ['id', 'name', 'master_bonus', 'numb_av_spells', 'descr_id']
            self.listView.setHorizontalHeaderLabels(
                ["ID", "Название", "Бонус мастерства", "Кол-во доступных заклинаний", "ID описания"])
        if result == "Оружие":
            table = Weapon
            line = session.query(Weapon).count()
            self.ui.listView.setColumnCount(6)
            self.ui.qTable = session.query(Weapon).all()
            collums = ['id', 'name', 'price', 'damage', 'weight', 'weap_t_id']
            self.ui.listView.setHorizontalHeaderLabels(["ID", "Название", "Цена", "Урон", "Вес", "ID типа"])
        if result == "Броня":
            table = Armor
            line = session.query(Armor).count()
            self.ui.listView.setColumnCount(6)
            self.ui.qTable = session.query(Armor).all()
            collums = ['id', 'name', 'price', 'steal_hindr', 'weight', 'arm_t_id']
            self.ui.listView.setHorizontalHeaderLabels(["ID", "Название", "Цена", "Громкий", "Вес", "ID типа"])
        if result == "Таблица заклинаний":
            table = Spell_table
            line = session.query(Spell_table).count()
            self.ui.listView.setColumnCount(6)
            self.ui.qTable = session.query(Spell_table).all()
            collums = ['id', 'name', 'level', 'distance', 'duration', 'descr_id']
            self.ui.listView.setHorizontalHeaderLabels(
                ["ID", "Название", "Уровень", "Дистанция", "Длительность", "ID описания"])
        if result == "Связи типов оружия и классов":
            table = Relat_table_t_weap_t_cl
            line = 21  # session.query(Relat_table_t_weap_t_cl).count()
            self.ui.listView.setColumnCount(3)
            self.ui.qTable = session.query(Relat_table_t_weap_t_cl).all()
            collums = ['id', 'weap_t_id', 'class_id']
            self.ui.listView.setHorizontalHeaderLabels(["ID", "ID типа оружия", "ID класса"])
        if result == "Связи типов доспехов и классов":
            table = Relat_table_t_arm_t_cl
            line = 25  # session.query(Relat_table_t_arm_t_cl).count()
            self.ui.listView.setColumnCount(3)
            self.ui.qTable = session.query(Relat_table_t_arm_t_cl).all()
            collums = ['id', 'arm_t_id', 'class_id']
            self.ui.listView.setHorizontalHeaderLabels(["ID", "ID типа брони", "ID класса"])
        if result == "Связи заклинаний и классов":
            table = Relat_table_t_spell_cl
            line = 28  # session.query(Relat_table_t_spell_cl).count()
            self.ui.listView.setColumnCount(3)
            self.ui.qTable = session.query(Relat_table_t_spell_cl).all()
            collums = ['id', 'spell_id', 'class_id']
            self.ui.listView.setHorizontalHeaderLabels(["ID", "ID заклинания", "ID класса"])
        if result == "Персонаж":
            table = Character
            line = session.query(Character).count()
            self.ui.listView.setColumnCount(13)
            self.ui.qTable = session.query(Character).all()
            collums = ['id', 'name', 'power', 'agility', 'body_type', 'intellect', 'wisdom', 'charisma', 'acc_id',
                       'var_races_id', 'class_id', 'weap_id', 'arm_id']
            self.listView.setHorizontalHeaderLabels(
                ["ID", "Имя", "Сила", "Ловкость", "Телосложение", "Интеллект", "Мудрость", "Харизма", "ID аккаунта",
                 "ID разновидности расы", "ID класса", "ID оружия", "ID брони"])

        self.ui.listView.setRowCount(line)
        sort = [0] * line
        j = 0
        for i in collums:
            if i != 'id':
                self.ui.comboBox_2.addItem(i)
        for i in session.query(table).all():
            sort[j] = i.id
            j += 1
        sort.sort()
        for i in sort:
            self.ui.comboBox_3.addItem(str(i))
        perem = 0
        j = -1
        for i in sort:
            j += 1
            for row, form in enumerate(self.ui.qTable):
                col = 0
                for c in collums:
                    for k, v in vars(form).items():
                        if c == k:
                            if c == 'id':
                                perem = v
                            if ((c == 'id') & (v == i)) | ((c != 'id') & (perem == i)):
                                self.ui.listView.setItem(j, col, QTableWidgetItem(str(v)))
                                col += 1
        self.ui.listView.setStyleSheet("selection-color: rgb(255, 0, 127);\n"
                                       "selection-background-color: rgb(85, 255, 127);")
        self.ui.listView.resizeColumnsToContents()

    def change_table(self):
        self.ui.statusbar.clearMessage()
        if self.ui.prov == 0:
            self.ui.prov = 1
        result = self.ui.comboBox.currentText()
        change = self.ui.comboBox_4.currentText()
        stri = int(self.ui.comboBox_3.currentText())
        stlb = self.ui.comboBox_2.currentText()
        text = self.ui.textBrowser.toPlainText()
        lis = text.split(',')
        table = Weapon
        user_setting = insert(table).values(id=session.query(table).count() + 1, name=text)
        query = session.query(table).filter(table.id == 1)
        try:
            if result == "Типы оружия":
                table = weapon_types
                if change == "Добавить строку":
                    user_setting = table(id=session.query(table).count() + 1, name=text)
                if change == "Обновить элемент":
                    query = session.query(table).filter(table.id == stri).first()
                    query.name = text
            if result == "Типы брони":
                table = armor_types
                if change == "Добавить строку":
                    user_setting = table(id=session.query(table).count() + 1, name=text)
                if change == "Обновить элемент":
                    query = session.query(table).filter(table.id == stri).first()
                    query.name = text
            if result == "Статусы пользователя":
                table = user_status
                if change == "Добавить строку":
                    user_setting = table(id=session.query(table).count() + 1, status=text)
                if change == "Обновить элемент":
                    query = session.query(table).filter(table.id == stri).first()
                    query.status = text
            if result == "Описания":
                table = descriptions
                if change == "Добавить строку":
                    user_setting = table(id=session.query(table).count() + 1, field=text)
                if change == "Обновить элемент":
                    query = session.query(table).filter(table.id == stri).first()
                    query.field = text
            if result == "Расы":
                table = Races
                if change == "Добавить строку":
                    user_setting = table(id=session.query(table).count() + 1, name=lis[0], incr_char=lis[1],
                                         worldview=lis[2], size=lis[3], speed=int(lis[4]), descr_id=int(lis[5]))
                if change == "Обновить элемент":
                    query = session.query(table).filter(table.id == stri).first()
                    if stlb == "name":
                        query.name = text
                    if stlb == "incr_char":
                        query.incr_char = text
                    if stlb == "worldview":
                        query.worldview = text
                    if stlb == "size":
                        query.size = text
                    if stlb == "speed":
                        query.speed = int(text)
                    if stlb == "descr_id":
                        query.descr_id = int(text)
            if result == "Разновидности рас":
                table = var_races
                if change == "Добавить строку":
                    user_setting = table(id=session.query(table).count() + 1, name=lis[0], incr_char=lis[1],
                                         add_feat=lis[2], rac_id=int(lis[3]), descr_id=int(lis[4]))
                if change == "Обновить элемент":
                    query = session.query(table).filter(table.id == stri).first()
                    if stlb == "name":
                        query.name = text
                    if stlb == "incr_char":
                        query.incr_char = text
                    if stlb == "add_feat":
                        query.add_feat = text
                    if stlb == "rac_id":
                        query.rac_id = text
                    if stlb == "descr_id":
                        query.descr_id = int(text)
            if result == "Аккаунты":
                table = Accounts
                if change == "Добавить строку":
                    user_setting = table(id=session.query(table).count() + 1, login=lis[0], password=lis[1],
                                         stat_id=int(lis[2]))
                if change == "Обновить элемент":
                    query = session.query(table).filter(table.id == stri).first()
                    if stlb == "login":
                        query.login = text
                    if stlb == "password":
                        query.password = text
                    if stlb == "stat_id":
                        query.stat_id = int(text)
            if result == "Классы":
                table = Classes
                if change == "Добавить строку":
                    user_setting = table(id=session.query(table).count() + 1, name=lis[0],
                                         master_bonus=int(lis[1]),
                                         numb_av_spells=int(lis[2]), descr_id=int(lis[3]))
                if change == "Обновить элемент":
                    query = session.query(table).filter(table.id == stri).first()
                    if stlb == "name":
                        query.name = text
                    if stlb == "master_bonus":
                        query.master_bonus = int(text)
                    if stlb == "numb_av_spells":
                        query.numb_av_spells = int(text)
                    if stlb == "descr_id":
                        query.descr_id = int(text)
            if result == "Оружие":
                table = Weapon
                if change == "Добавить строку":
                    user_setting = table(id=session.query(table).count() + 1, name=lis[0], price=int(lis[1]),
                                         damage=int(lis[2]), weight=int(lis[3]), weap_t_id=int(lis[4]))
                if change == "Обновить элемент":
                    query = session.query(table).filter(table.id == stri).first()
                    if stlb == "name":
                        query.name = text
                    if stlb == "price":
                        query.price = int(text)
                    if stlb == "damage":
                        query.damage = int(text)
                    if stlb == "weight":
                        query.weight = int(text)
                    if stlb == "weap_t_id":
                        query.weap_t_id = int(text)
            if result == "Броня":
                table = Armor
                if change == "Добавить строку":
                    user_setting = table(id=session.query(table).count() + 1, name=lis[0], price=int(lis[1]),
                                         steal_hindr=bool(lis[2]), weight=int(lis[3]), arm_t_id=int(lis[4]))
                if change == "Обновить элемент":
                    query = session.query(table).filter(table.id == stri).first()
                    if stlb == "name":
                        query.name = text
                    if stlb == "price":
                        query.price = int(text)
                    if stlb == "steal_hindr":
                        query.steal_hindr = bool(text)
                    if stlb == "weight":
                        query.weight = int(text)
                    if stlb == "arm_t_id":
                        query.arm_t_id = int(text)
            if result == "Таблица заклинаний":
                table = Spell_table
                if change == "Добавить строку":
                    user_setting = table(id=session.query(table).count() + 1, name=lis[0], level=int(lis[1]),
                                         distance=int(lis[2]), duration=int(lis[3]), descr_id=int(lis[4]))
                if change == "Обновить элемент":
                    query = session.query(table).filter(table.id == stri).first()
                    if stlb == "name":
                        query.name = text
                    if stlb == "level":
                        query.level = int(text)
                    if stlb == "distance":
                        query.distance = int(text)
                    if stlb == "duration":
                        query.duration = int(text)
                    if stlb == "descr_id":
                        query.descr_id = int(text)
            if result == "Связи типов оружия и классов":
                table = Relat_table_t_weap_t_cl
                if change == "Добавить строку":
                    user_setting = table(id=session.query(table).count() + 1, weap_t_id=int(lis[0]),
                                         class_id=int(lis[1]))
                if change == "Обновить элемент":
                    query = session.query(table).filter(table.id == stri).first()
                    if stlb == "weap_t_id":
                        query.weap_t_id = int(text)
                    if stlb == "class_id":
                        query.class_id = int(text)
            if result == "Связи типов доспехов и классов":
                table = Relat_table_t_arm_t_cl
                if change == "Добавить строку":
                    user_setting = table(id=session.query(table).count() + 1, arm_t_id=int(lis[0]),
                                         class_id=int(lis[1]))
                if change == "Обновить элемент":
                    query = session.query(table).filter(table.id == stri).first()
                    if stlb == "arm_t_id":
                        query.arm_t_id = int(text)
                    if stlb == "class_id":
                        query.class_id = int(text)
            if result == "Связи заклинаний и классов":
                table = Relat_table_t_spell_cl
                if change == "Добавить строку":
                    user_setting = table(id=session.query(table).count() + 1, spell_id=int(lis[0]),
                                         class_id=int(lis[1]))
                if change == "Обновить элемент":
                    query = session.query(table).filter(table.id == stri).first()
                    if stlb == "spell_id":
                        query.spell_id = int(text)
                    if stlb == "class_id":
                        query.class_id = int(text)
            if result == "Персонаж":
                table = Character
                if change == "Добавить строку":
                    user_setting = table(id=session.query(table).count() + 1, name=lis[0], power=int(lis[1]),
                                         agility=int(lis[2]), body_type=int(lis[3]), intellect=int(lis[4]),
                                         wisdom=int(lis[5]), charisma=int(lis[6]), acc_id=int(lis[7]),
                                         var_races_id=int(lis[8]), class_id=int(lis[9]), weap_id=int(lis[10]),
                                         arm_id=int(lis[11]))
                if change == "Обновить элемент":
                    query = session.query(table).filter(table.id == stri).first()
                    if stlb == "name":
                        query.name = text
                    if stlb == "power":
                        query.power = int(text)
                    if stlb == "agility":
                        query.agility = int(text)
                    if stlb == "body_type":
                        query.body_type = int(text)
                    if stlb == "intellect":
                        query.intellect = int(text)
                    if stlb == "wisdom":
                        query.wisdom = int(text)
                    if stlb == "charisma":
                        query.charisma = int(text)
                    if stlb == "acc_id":
                        query.acc_id = int(text)
                    if stlb == "var_races_id":
                        query.var_races_id = int(text)
                    if stlb == "class_id":
                        query.class_id = int(text)
                    if stlb == "weap_id":
                        query.weap_id = int(text)
                    if stlb == "arm_id":
                        query.arm_id = int(text)
            if change == "Удалить строку":
                session.query(table).filter_by(id=stri).delete(synchronize_session=False)
            if change == "Добавить строку":
                session.add(user_setting)

            self.show_table()
        except:
            self.ui.statusbar.showMessage("Произошла ошибка")

    def confirm_change(self):
        if self.ui.prov != 0:
            session.commit()
            self.ui.prov = 0
            self.show_table()
        else:
            self.ui.statusbar.showMessage("Сначала внесите изменение в таблицу")

    def undo_change(self):
        if self.ui.prov != 0:
            session.rollback()
            self.ui.prov = 0
            self.show_table()
        else:
            self.ui.statusbar.showMessage("Сначала внесите изменение в таблицу")

    def exit_db_panel(self):
        self.hide()
        self.ui.app.exit()


class log_panel(QMainWindow):
    def __init__(self, parent=None):
        super(log_panel, self).__init__(parent)
        self.ui = login_panell()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.inter_to_app())
        self.ui.pushButton_2.clicked.connect(lambda: self.create_acc())

    def inter_to_app(self):
        log = self.ui.textEdit.toPlainText()
        pasw = self.ui.textEdit_2.toPlainText()
        if log == "":
            self.ui.statusbar.showMessage("Введите логин")
            return
        if pasw == "":
            self.ui.statusbar.showMessage("Введите пароль")
            return
        for i in session.query(Accounts).all():
            if log == i.login:
                if pasw == i.password:
                    self.hide()
                    if i.stat_id == 1:
                        dialog = Admin_db_Panel(parent=self)
                        dialog.show()
                    else:
                        dialog = Admin_db_Panel(parent=self)
                        dialog.show()
                else:
                    self.ui.statusbar.showMessage("Введён неверный пароль")
        self.ui.statusbar.showMessage("Введено несуществующее имя пользователя")

    def create_acc(self):
        log = self.ui.textEdit.toPlainText()
        pasw = self.ui.textEdit_2.toPlainText()
        if log == "":
            self.ui.statusbar.showMessage("Введите логин для нового пользователя")
            return
        if pasw == "":
            self.ui.statusbar.showMessage("Введите пароль для нового пользователя")
            return
        for i in session.query(Accounts).all():
            if log == i.login:
                self.ui.statusbar.showMessage("Пользователь с таким логином уже существует")
                return
        user_setting = Accounts(id=session.query(Accounts).count() + 1, login=log, password=pasw,
                                stat_id=int(2))
        session.add(user_setting)
        session.commit()
        self.hide()
        dialog = Admin_db_Panel(parent=self)
        dialog.show()
