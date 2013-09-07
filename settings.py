#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# settings file of all programs.

# seconds between price queries.
time_interval = 1

# you need an e-mail account with an SSL-enabled SMTP server. consult your e-mail provider for following information.
smtp_ssl_address = 'smtp.somewhere.com'
smtp_ssl_port = 123
smtp_ssl_username = 'somebody'
smtp_ssl_password = '123456'
email_address = 'somebody@somewhere.com'

# if last price goes beyond range, a mail is sent.
# if you want to disable mail alert, set both to impractical values.
price_lowerbound = 700
price_upperbound = 750

# file will be created if not exist, updated if exists.
# not needed if you don't use crawler.py
crawler_output_path = 'btcchina.db'