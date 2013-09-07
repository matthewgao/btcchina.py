#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# fetch all trading records from BTCChina and store them in an sqlite3 database.
# creates the database if it does not exist. updates it if it exists.

from settings import crawler_output_path
from urllib.request import urlopen
import sqlite3
import json
from ast import literal_eval

def type_conv(type_str):
    if type_str == 'sell':
        return 0
    if type_str == 'buy':
        return 1

if __name__ == '__main__':
    con = sqlite3.connect(crawler_output_path)
    cur = con.cursor()
    cur.execute('SELECT name FROM sqlite_master')
    if not cur.fetchall():
        cur.execute('CREATE TABLE BTCChina_history_data(date INTEGER,price REAL,amount REAL,tid INTEGER PRIMARY KEY ASC,type INTEGER)')
        i = 0
    else:
        cur.execute('SELECT MAX(tid) FROM BTCChina_history_data')
        i = cur.fetchone()[0]
    while True:
        remote_file = urlopen('https://data.btcchina.com/data/historydata?since=%d'%i)
        remote_data = remote_file.read()
        remote_file.close()
        remote_data = json.loads(str(remote_data, encoding='utf-8'))
        if not remote_data:
            break
        tid_set = set()
        for record in remote_data:
            if literal_eval(record['tid']) not in tid_set:
                cur.execute('INSERT INTO BTCChina_history_data(date,price,amount,tid,type) VALUES(%s,%f,%f,%s,%d)'%(
                    record['date'],record['price'],record['amount'],record['tid'],type_conv(record['type'])
                ))
            tid_set.add(literal_eval(record['tid']))
        print('tid %d~%d updated.'%(i,max(tid_set)))
        i = max(tid_set)
    con.commit()
    con.close()