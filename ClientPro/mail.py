from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    # 邮件地址格式化
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


SMTPSVR = 'smtp.126.com' #smtp 服务器
who = 'one@one.com'
info = {
    'From':who,
    'To':who,
    'Subject':'test message',
    'Content':'this is a test email sended by python3.6'
}

msg = MIMEText(info['Content'], 'html', 'utf-8')
msg['From'] = _format_addr(info['From'])
msg['To'] = _format_addr(info['To'])
msg['Subject'] = Header(info['Subject'], 'utf-8').encode()

sendSvr = SMTP(SMTPSVR, 25)
sendSvr.login('user','password') # 更换成自己的email 用户名和密码
errs = sendSvr.sendmail(who, 'one@one.com', msg.as_string())
sendSvr.quit()
assert len(errs) == 0, errs
