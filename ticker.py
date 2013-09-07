#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# query price data from BTCChina.

from urllib.request import urlopen
from ast import literal_eval
import json

def instance():
    # returns something like {"high":738.88,"low":689.10,"buy":713.50,"sell":717.30,"last":717.41,"vol":4797.32000000}
    remote_file = urlopen('https://btcchina.com/bc/ticker')
    remote_data = remote_file.read()
    remote_file.close()
    remote_data = json.loads(str(remote_data,encoding='utf-8'))['ticker']
    remote_data = {key:literal_eval(remote_data[key]) for key in remote_data}
    return remote_data