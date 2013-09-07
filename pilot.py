#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# automatic price monitoring program.
# prints price data to the terminal whenever changed.
# sends alert mail when last price slips out of range. check settings.py for details

from settings import time_interval, price_lowerbound, price_upperbound
from ticker import instance
from mailer import construct_text, send_mail

import time
from datetime import datetime

if __name__ == '__main__':
    ans = None
    while True:
        inst = instance()
        if inst != ans:
            print('%s\n%s\n'%(str(datetime.now()),construct_text(inst)))
            if inst['last']<price_lowerbound or inst['last']>price_upperbound:
                send_mail(inst)
            ans = inst
        time.sleep(time_interval)