from sqlalchemy import create_engine, insert, delete, update
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Подключение к серверу PostgreSQL на localhost
engine = create_engine("postgresql+psycopg2://postgres:@localhost/game_app")
conn = engine.connect()


# Типы оружия
class weapon_types(Base):
    __tablename__ = 'weapon_types'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))

    def __repr__(self):
        return f'{self.id} {self.name}'


# Типы защиты
class armor_types(Base):
    __tablename__ = 'armor_types'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))

    def __repr__(self):
        return f'{self.id} {self.name}'


# Статусы пользователя
class user_status(Base):
    __tablename__ = 'user_status'
    id = Column(Integer, primary_key=True)
    status = Column(String(40))

    def __repr__(self):
        return f'{self.id} {self.status}'


# Описания
class descriptions(Base):
    __tablename__ = 'descriptions'
    id = Column(Integer, primary_key=True)
    field = Column(String(500))

    def __repr__(self):
        return f'{self.id} {self.field}'


# Расы
class Races(Base):
    __tablename__ = 'races'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    incr_char = Column(String(40))
    worldview = Column(String(500))
    size = Column(String(500))
    speed = Column(Integer)
    descr_id = Column(Integer, ForeignKey('descriptions.id'))

    def __repr__(self):
        return f'{self.id} {self.name} {self.incr_char} {self.worldview} {self.size} {self.speed} {self.descr_id}'


# Разновидности рас
class var_races(Base):
    __tablename__ = 'var_races'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    incr_char = Column(String(40))
    add_feat = Column(String(500))
    rac_id = Column(Integer, ForeignKey('Races.id'))
    descr_id = Column(Integer, ForeignKey('descriptions.id'))

    def __repr__(self):
        return f'{self.id} {self.name} {self.incr_char} {self.add_feat} {self.rac_id} {self.descr_id}'


# Аккаунты
class Accounts(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    login = Column(String(40))
    password = Column(String(10))
    stat_id = Column(Integer, ForeignKey('user_status.id'))

    def __repr__(self):
        return f'{self.id} {self.login} {self.password} {self.stat_id}'


# Классы
class Classes(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    master_bonus = Column(Integer)
    numb_av_spells = Column(Integer)
    descr_id = Column(Integer, ForeignKey('descriptions.id'))

    def __repr__(self):
        return f'{self.id} {self.name} {self.master_bonus} {self.numb_av_spells} {self.descr_id}'


# Оружие
class Weapon(Base):
    __tablename__ = 'weapon'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    price = Column(Integer)
    damage = Column(Integer)
    weight = Column(Integer)
    weap_t_id = Column(Integer, ForeignKey('weapon_types.id'))

    def __repr__(self):
        return f'{self.id} {self.name} {self.price} {self.damage} {self.weight} {self.weap_t_id}'


# Броня
class Armor(Base):
    __tablename__ = 'armor'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    price = Column(Integer)
    steal_hindr = Column(Boolean)
    weight = Column(Integer)
    arm_t_id = Column(Integer, ForeignKey('armor_types.id'))

    def __repr__(self):
        return f'{self.id} {self.name} {self.price} {self.steal_hindr} {self.weight} {self.arm_t_id}'


# Таблица заклинаний
class Spell_table(Base):
    __tablename__ = 'spell_table'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    level = Column(Integer)
    distance = Column(Integer)
    duration = Column(Integer)
    descr_id = Column(Integer, ForeignKey('descriptions.id'))

    def __repr__(self):
        return f'{self.id} {self.name} {self.level} {self.distance} {self.duration} {self.descr_id}'


# Таблица связей типов оружия и классов
class Relat_table_t_weap_t_cl(Base):
    __tablename__ = 'relat_table_t_weap_t_cl'
    id = Column(Integer, primary_key=True)
    weap_t_id = Column(Integer, ForeignKey('weapon_types.id'))
    class_id = Column(Integer, ForeignKey('Classes.id'))

    def __repr__(self):
        return f'{self.id} {self.weap_t_id} {self.class_id}'


# Таблица связей типов доспехов и классов
class Relat_table_t_arm_t_cl(Base):
    __tablename__ = 'relat_table_t_arm_t_cl'
    id = Column(Integer, primary_key=True)
    arm_t_id = Column(Integer, ForeignKey('armor_types.id'))
    class_id = Column(Integer, ForeignKey('Classes.id'))

    def __repr__(self):
        return f'{self.id} {self.arm_t_id} {self.class_id}'


# Таблица связей заклинаний и классов
class Relat_table_t_spell_cl(Base):
    __tablename__ = 'relat_table_t_spell_cl'
    id = Column(Integer, primary_key=True)
    spell_id = Column(Integer, ForeignKey('spell_table.id'))
    class_id = Column(Integer, ForeignKey('classes.id'))

    def __repr__(self):
        return f'{self.id} {self.spell_id} {self.class_id}'


# Персонаж
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    power = Column(Integer)
    agility = Column(Integer)
    body_type = Column(Integer)
    intellect = Column(Integer)
    wisdom = Column(Integer)
    charisma = Column(Integer)
    acc_id = Column(Integer, ForeignKey('accounts.id'))
    var_races_id = Column(Integer, ForeignKey('var_races.id'))
    class_id = Column(Integer, ForeignKey('classes.id'))
    weap_id = Column(Integer, ForeignKey('weapon.id'))
    arm_id = Column(Integer, ForeignKey('armor.id'))

    def __repr__(self):
        return f'{self.id} {self.name} {self.power} {self.agility} {self.body_type} {self.intellect} {self.wisdom} {self.charisma} {self.acc_id} {self.var_races_id} {self.class_id} {self.weap_id} {self.arm_id}'


Session = sessionmaker(bind=engine)
session = Session()
