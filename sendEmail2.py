# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:27:05 2017

@author: MFX
"""

# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(),addr.encode('utf-8') if isinstance(addr, unicode) else addr))

# 收发邮件人信息，邮箱配置信息
from_addr = 'fmeng@hantak.cn'#raw_input('From: ')
password = 'wjf19890221'#raw_input('Password: ')
to_addr = '512537531@qq.com'#raw_input('To: ')
smtp_server = 'smtp.exmail.qq.com'#raw_input('SMTP server: ')


#显示邮件主题、发件人、收件人等信息
#msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')


#发送HTML邮件
#==============================================================================
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')
# msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
# msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()
#==============================================================================

# 如何添加附件
# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('E:\\picture\\002564c1964d1393d73529.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
#==============================================================================

# 发送邮件
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()