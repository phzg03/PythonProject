from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

SENDER = 'zhanggao'
TOER = 'zhanggao'

def make_mpa_msg():
    email = MIMEMultipart('alternative')
    text = MIMEText('email by python\r\n', 'plain')
    email.attach(text)
    html = MIMEText('<html><body><h4>this is a test email, send by python</h4></body></html>', 'plain')
    email.attach(html)
    return email

def make_img_msg(fn):
    f = open(fn, 'r')
    data = f.read()
    f.close()
    email = MIMEImage(data, name=fn)
    email.add_header('Content-Disposition', 'attachment;filename="%s"' % fn)
    return email


def sendmsg(fr, to, msg):
    s = SMTP('localhost')
    errs = s.sendmail(fr, to, msg)
    s.quit()

#
# if __name__ == '__main__':
#     print('Sending multipart alternative msg...')
#     msg = make_mpa_msg()
#     msg['From'] = SENDER
#     msg['To'] = TOER
#     msg['Subject'] = 'multipart alternative test'
#     sendmsg(SENDER, TOER, msg.as_string())
#
#     print('Sending img msg')
#     msg = make_img_msg('C:/Users/lenovo/Pictures/Saved Pictures/我带你飞吧.jpg')
#     msg['From'] = SENDER
#     msg['To'] = TOER
#     msg['Subject'] = 'image file test'
#     sendmsg(SENDER, TOER, msg.as_string())
