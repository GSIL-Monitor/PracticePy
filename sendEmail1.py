# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:14:37 2017

@author: MFX
"""

from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 输入Email地址和口令:
from_addr = raw_input('From: ')# fmeng@hantak.cn
password = raw_input('Password: ')
# 输入SMTP服务器地址:
smtp_server = raw_input('SMTP server: ')# smtp.exmail.qq.com
# 输入收件人地址:
to_addr = raw_input('To: ')

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()