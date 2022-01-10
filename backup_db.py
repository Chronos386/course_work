import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import time
from subprocess import PIPE, Popen


def send_email(filepath):
    addr_to = "popersoniy@gmail.com"
    msg_subj = "Резервная копия базы данных"
    msg_text = "Копия: "

    addr_from = "popersoniy@gmail.com"
    password = "**********"

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


def CreateFileName(dbms):
    fileTime = time.localtime(time.time())

    year = fileTime.tm_year
    month = fileTime.tm_mon
    day = fileTime.tm_mday
    hour = fileTime.tm_hour
    minute = fileTime.tm_min
    second = fileTime.tm_sec

    filename = f"{month}-{day}-{year}_{hour}:{minute}:{second}_{dbms}_dump.dmp"
    return filename


def DumpPostgreSql():
    host_name = "localhost"
    database_name = "game_app"
    user_name = "postgres"
    database_password = ""
    filename = CreateFileName('game_app')
    command = f'pg_dump -h {host_name} -d {database_name} -U {user_name} -p 5432 -Fc -f {filename}'
    p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    p.communicate(bytes('{}\n'.format(database_password), encoding='utf8'))
    send_email(f"./{filename}")
    os.remove(f"./{filename}")
