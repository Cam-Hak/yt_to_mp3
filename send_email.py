import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def send_mail(
    send_from,
    send_to,
    subject,
    text,
    file=None,
    server="smtp.gmail.com",
    port=587,
    username=None,
    password=None,
):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg["From"] = send_from
    msg["To"] = COMMASPACE.join(send_to)
    msg["Date"] = formatdate(localtime=True)
    msg["Subject"] = subject

    msg.attach(MIMEText(text))

    if file:
        with open(file, "rb") as fil:
            part = MIMEApplication(fil.read(), Name=basename(file))
        part["Content-Disposition"] = f'attachment; filename="{basename(file)}"'
        msg.attach(part)

    # Connect to Gmail SMTP server
    smtp = smtplib.SMTP(server, port)
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
