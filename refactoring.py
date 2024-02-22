import email
import smtplib
import imaplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
    def __init__(self, smtp: str, imap: str, port : int) -> None:
        self.smtp = smtp
        self.imap = imap
        self.port = port

    def send_message(self, login: str, password: str, subject: str, recipients: str, message: str):
        # send message
        msg = MIMEMultipart()
        msg['From'] = login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(self.smtp, self.port)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(login, password)
        ms.sendmail(login, ms, msg.as_string())

        ms.quit()
        # send end
        return

    def receive_message(self, login, password, header):
        # receive
        mail = imaplib.IMAP4_SSL(self.imap)
        mail.login(login, password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        # end receive
        return email_message


if __name__ == '__main__':
    my_email = Email('smtp.gmail.com', 'imap.gmail.com', 587)
    my_email.send_message('login@gmail.com', 'qwerty', 'Subject',
                          ['vasya@email.com', 'petya@email.com'], 'Message')
    my_email.receive_message('login@gmail.com', 'qwerty', None)
