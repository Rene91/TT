#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:39:57 2020

@author: rene
"""

# Estos paquetes los usaremos para analizar y visualizar los resultados
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../../2.LimpiezaDatos/2.filtro_polaridad_clase.csv', sep=';')
df = df.drop(df.columns[[0]], axis='columns') #eliminamos columna


############# FILTRADO POR RANGO
cabecera = "2016-2019"
rango_fecha = (df['FECHA'] >= '2016-01-01') & (df['FECHA'] <= '2021-01-01')
df=df.loc[rango_fecha]



######################### PROMEDIOS PARA CADA POLARIDAD
positivo = df.loc[df['FILTRO_2_CLASE_ES']=="POS"]
media_positivo = "{00:.00f}%".format((positivo['FILTRO_2_CLASE_ES'].count() / df['FILTRO_2_CLASE_ES'].count()) * 100)

negativo = df.loc[df['FILTRO_2_CLASE_ES']=="NEG"]
media_negativo = "{00:.00f}%".format((negativo['FILTRO_2_CLASE_ES'].count() / df['FILTRO_2_CLASE_ES'].count()) * 100)

neutro = df.loc[df['FILTRO_2_CLASE_ES']=="NEU"]
media_neutro = "{00:.00f}%".format((neutro['FILTRO_2_CLASE_ES'].count() / df['FILTRO_2_CLASE_ES'].count()) * 100)


##################  TEXTO DE LA GRAFICA
 #axes = plt.gca()
#axes.set_ylim([-1, 1])
#### 1.3 eje X y 8000 eje Y
x = 1.3
y = float("{00:.00f}".format((df['FILTRO_2_CLASE_ES'].count()) * 0.43))#obtenemos el 43% del total de los datos para poner el texto
plt.text(x, y, 
             "POS:  " + str(positivo['FILTRO_2_CLASE_ES'].count()) + " ---  " + str(media_positivo) + 
             "\nNEG:  " + str(negativo['FILTRO_2_CLASE_ES'].count()) + " ---  " + str(media_negativo) + 
             "\nNUE:  " + str(neutro['FILTRO_2_CLASE_ES'].count()) + " ---  " + str(media_neutro), 
             fontsize=8, 
             bbox = dict(facecolor='none', 
                         edgecolor='red', 
                        boxstyle='square, pad = 1'))
    
df.FILTRO_2_CLASE_ES.value_counts().plot(kind='bar', color=['blue','green', 'red'])
plt.title('Polaridad del FIAVL del año ' + cabecera)
plt.xlabel('Etiquetas de los tweets ')
plt.ylabel('Número de Tweets:  ' + str(df['FILTRO_2_CLASE_ES'].count()))
plt.show()