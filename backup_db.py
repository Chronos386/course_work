import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import psycopg2
import sys
import time


def send_email(filepath):
    addr_to = "popersoniy@gmail.com"
    msg_subj = "Резервная копия базы данных"
    msg_text = "Копия: "

    addr_from = "popersoniy@gmail.com"
    password = "**************"

    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = addr_to
    msg['Subject'] = msg_subj

    body = msg_text
    msg.attach(MIMEText(body, 'plain'))

    add_file(msg, filepath)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()


def add_file(msg, filepath):
    filename = os.path.basename(filepath)
    if os.path.isfile(filepath):
        ctype, encoding = mimetypes.guess_type(filepath)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        if maintype == 'text':
            with open(filepath) as fp:
                file = MIMEText(fp.read(), _subtype=subtype)
                fp.close()
        elif maintype == 'image':
            with open(filepath, 'rb') as fp:
                file = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()
        elif maintype == 'audio':
            with open(filepath, 'rb') as fp:
                file = MIMEAudio(fp.read(), _subtype=subtype)
                fp.close()
        else:
            with open(filepath, 'rb') as fp:
                file = MIMEBase(maintype, subtype)
                file.set_payload(fp.read())
                fp.close()
            encoders.encode_base64(file)
        file.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(file)


# "voff.chernih@yandex.ru"
#ubtyhhdoejtyutex


def CreateFileName(dbms):
    fileTime = time.localtime(time.time())

    year = fileTime.tm_year
    month = fileTime.tm_mon
    day = fileTime.tm_mday
    hour = fileTime.tm_hour
    minute = fileTime.tm_min
    second = fileTime.tm_sec

    filename = f"{month}-{day}-{year}_{hour}:{minute}:{second}_{dbms}_dump.sql"
    return filename


def DumpPostgreSql():
    con = None
    try:
        con = psycopg2.connect(database='game_app', user='postgres', password='local', port='5432')
        cur = con.cursor()
        filename = CreateFileName('game_app')
        f = open(filename, 'w')
        f.write(
            "CREATE TABLE weapon_types(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    Name VARCHAR (40) NOT NULL\n);\n\n")
        f.write(
            "CREATE TABLE armor_types(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    Name VARCHAR (40) NOT NULL\n);\n\n")
        f.write(
            "CREATE TABLE user_status(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    status VARCHAR (40) NOT NULL\n);\n\n")
        f.write(
            "CREATE TABLE descriptions(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    field VARCHAR (500) NOT NULL\n);\n\n")
        f.write("CREATE TABLE Races(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    Name VARCHAR (40) NOT NULL,\n"
                "    Incr_char VARCHAR (40) NOT NULL,\n    Worldview VARCHAR (500) NOT NULL,\n    size VARCHAR (500) NOT NULL,"
                "\n    Speed INTEGER NOT NULL,\n    descr_ID BIGSERIAL NOT NULL,\n    FOREIGN KEY(descr_ID) "
                "REFERENCES descriptions(ID)\n);\n\n")
        f.write("CREATE TABLE var_races(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    Name VARCHAR (40) NOT NULL,\n"
                "    Incr_char VARCHAR (40) NOT NULL,\n    Add_feat VARCHAR (500) NOT NULL,\n    rac_ID BIGSERIAL NOT NULL,"
                "\n    FOREIGN KEY(rac_ID) REFERENCES Races(ID),\n    descr_ID BIGSERIAL NOT NULL,\n    FOREIGN KEY(descr_ID) "
                "REFERENCES descriptions(ID)\n);\n\n")
        f.write("CREATE TABLE Accounts(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    Login VARCHAR (40) NOT NULL,\n"
                "    Password VARCHAR (10) NOT NULL,\n    stat_ID BIGSERIAL NOT NULL,\n    FOREIGN KEY(stat_ID) REFERENCES "
                "user_status(ID)\n);\n\n")
        f.write("CREATE TABLE Classes(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    Name VARCHAR (40) NOT NULL,\n"
                "    Master_bonus INTEGER NOT NULL,\n    numb_av_spells INTEGER NOT NULL,\n    descr_ID BIGSERIAL NOT NULL,"
                "\n    FOREIGN KEY(descr_ID) REFERENCES descriptions(ID)\n);\n\n")
        f.write("CREATE TABLE Weapon(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    Name VARCHAR (40) NOT NULL,\n"
                "    Price INTEGER NOT NULL,\n    Damage INTEGER NOT NULL,\n    Weight INTEGER NOT NULL,"
                "\n    weap_t_ID BIGSERIAL NOT NULL,\n    FOREIGN KEY(weap_t_ID) REFERENCES weapon_types(ID)\n);\n\n")
        f.write("CREATE TABLE Armor(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    Name VARCHAR (40) NOT NULL,\n"
                "    Price INTEGER NOT NULL,\n    Steal_hindr BOOL NOT NULL,\n    Weight INTEGER NOT NULL,"
                "\n    arm_t_ID BIGSERIAL NOT NULL,\n    FOREIGN KEY(arm_t_ID) REFERENCES armor_types(ID)\n);\n\n")
        f.write("CREATE TABLE Spell_table(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    Name VARCHAR (40) NOT NULL,\n"
                "    level INTEGER NOT NULL,\n    Distance INTEGER NOT NULL,\n    Duration INTEGER NOT NULL,"
                "\n    descr_ID BIGSERIAL NOT NULL,\n    FOREIGN KEY(descr_ID) REFERENCES descriptions(ID)\n);\n\n")
        f.write(
            "CREATE TABLE Relat_table_t_weap_t_cl(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    weap_t_ID BIGSERIAL NOT NULL,\n"
            "    FOREIGN KEY(weap_t_ID) REFERENCES weapon_types(ID),\n    class_ID BIGSERIAL NOT NULL,\n    "
            "FOREIGN KEY(class_ID) REFERENCES Classes(ID)\n);\n\n")
        f.write(
            "CREATE TABLE Relat_table_t_arm_t_cl(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    arm_t_ID BIGSERIAL NOT NULL,\n"
            "    FOREIGN KEY(arm_t_ID) REFERENCES armor_types(ID),\n    class_ID BIGSERIAL NOT NULL,\n    "
            "FOREIGN KEY(class_ID) REFERENCES Classes(ID)\n);\n\n")
        f.write(
            "CREATE TABLE Relat_table_t_spell_cl(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    Spell_ID BIGSERIAL NOT NULL,\n"
            "    FOREIGN KEY(Spell_ID) REFERENCES Spell_table(ID),\n    class_ID BIGSERIAL NOT NULL,\n    "
            "FOREIGN KEY(class_ID) REFERENCES Classes(ID)\n);\n\n")
        f.write("CREATE TABLE Character(\n    ID BIGSERIAL NOT NULL PRIMARY KEY,\n    Name VARCHAR (40) NOT NULL,\n"
                "    Power INTEGER NOT NULL,\n    Agility INTEGER NOT NULL,\n    Body_type INTEGER NOT NULL,\n    Intellect "
                "INTEGER NOT NULL,\n    Wisdom INTEGER NOT NULL,\n    Charisma INTEGER NOT NULL,\n    acc_ID "
                "BIGSERIAL NOT NULL,\n    FOREIGN KEY(acc_ID) REFERENCES Accounts(ID),\n    var_races_ID BIGSERIAL "
                "NOT NULL,\n    FOREIGN KEY(var_races_ID) REFERENCES var_races(ID),\n    class_ID BIGSERIAL NOT NULL,\n"
                "    FOREIGN KEY(class_ID) REFERENCES Classes(ID),\n    weap_ID BIGSERIAL NOT NULL,\n    FOREIGN "
                "KEY(weap_ID) REFERENCES Weapon(ID),\n    arm_ID BIGSERIAL NOT NULL,\n    FOREIGN KEY(arm_ID) "
                "REFERENCES Armor(ID)\n);\n\n")
        for i in range(15):
            table_name = ""
            if i == 0:
                table_name = "weapon_types"
            if i == 1:
                table_name = "armor_types"
            if i == 2:
                table_name = "user_status"
            if i == 3:
                table_name = "descriptions"
            if i == 4:
                table_name = "Races"
            if i == 5:
                table_name = "var_races"
            if i == 6:
                table_name = "Accounts"
            if i == 7:
                table_name = "Classes"
            if i == 8:
                table_name = "Weapon"
            if i == 9:
                table_name = "Armor"
            if i == 10:
                table_name = "Spell_table"
            if i == 11:
                table_name = "Relat_table_t_weap_t_cl"
            if i == 12:
                table_name = "Relat_table_t_arm_t_cl"
            if i == 13:
                table_name = "Relat_table_t_spell_cl"
            if i == 14:
                table_name = "Character"
            cur.execute(f'SELECT * FROM {table_name}')
            for row in cur:
                f.write(f"insert into {table_name} values " + str(row) + ";\n")
            if i != 14:
                f.write("\n")
        time.sleep(3)
        send_email(f"./{filename}")
        os.remove(f"./{filename}")
    except psycopg2.DatabaseError(psycopg2.Error):
        print('Error %s' % psycopg2.Error)
        sys.exit(1)
    finally:
        if con:
            con.close()
