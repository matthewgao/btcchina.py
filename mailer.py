#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# send alert mail.

from settings import smtp_ssl_address, smtp_ssl_port, smtp_ssl_username, smtp_ssl_password, email_address
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
from datetime import datetime

def construct_text(price_dict):
    return 'Last price:¥%.2f\nBid price:¥%.2f\nAsk price:¥%.2f\nHigh price:¥%.2f\nLow price:¥%.2f\nVolume:%.3f\n'%(
        price_dict['last'],
        price_dict['buy'],
        price_dict['sell'],
        price_dict['high'],
        price_dict['low'],
        price_dict['vol']
    )

def construct_email(price_dict):
    msg = MIMEText(construct_text(price_dict))
    msg['Subject'] = 'BTCChina Price at %s'%str(datetime.now())
    msg['From'] = email_address
    msg['To'] = email_address
    return msg

def send_mail(price_dict):
    server = SMTP_SSL(smtp_ssl_address,smtp_ssl_port)
    server.login(smtp_ssl_username,smtp_ssl_password)
    server.send_message(construct_email(price_dict))
    server.quit()