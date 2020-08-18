#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 09:58:27 2020

@author: rene
"""


import pandas
import pandas as pd##trabaja con PDF
### LECTURA DEL csv
datos = pd.read_csv('ssssssssssssss.csv', sep=';')
df= pd.DataFrame(datos)##creacion dataframe interno
df = df.drop(df.columns[[0]], axis='columns') #eliminamos columna

print(df['ENLACE'])
df = df.drop_duplicates('ENLACE')
###creacion de csv
df.to_csv('2.filtro_traduccion.csv', sep=';' , encoding='utf-8-sig')
