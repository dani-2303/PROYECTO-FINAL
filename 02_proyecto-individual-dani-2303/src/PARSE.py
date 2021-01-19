# -*- coding: utf-8 -*-
'''
Created on 16 dic. 2020

@author: danie
'''
from datetime import datetime

def parse_str(cadena):
    return str(cadena)

def parse_int(numero):
    return int(numero)

def parse_date(cadena, formato=('%d/%m/%Y')):
    return datetime.strptime(cadena, formato).date()

def parse_time(cadena, formato = '%H:%M:%S'):
    return datetime.strptime(cadena, formato).time()

def parse_datetime(cadena, formato = '%d/%m/%Y-%H:%M:%S'):
    return datetime.strptime(cadena, formato)