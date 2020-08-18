#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 13:09:11 2020

@author: rene
"""

from time import sleep
from datetime import datetime
from textblob import TextBlob 
import matplotlib.pyplot as plt 
import pandas as pd##TRABAJAR CON PDF
import numpy as np


#Se define las listas que capturan la popularidad
popularidad_list = []
numeros_list = []
numero = 1


### LECTURA DEL csv
datos = pd.read_csv('../../2.LimpiezaDatos/2.filtro_polaridad_clase.csv', sep=';')
df= pd.DataFrame(datos)##creacion dataframe interno
df = df.drop(df.columns[[0]], axis='columns') #eliminamos columna


############# FILTRADO POR RANGO
cabecera = "2016-2019"
rango_fecha = (df['FECHA'] >= '2016-01-01') & (df['FECHA'] <= '2021-01-01')
df=df.loc[rango_fecha]

for dato in df.index:
    popularidad = float(df['FILTRO_2_POLARIDAD_ES'][dato])
    #popularidad = tweet_en.polarity
    popularidad_list.append(popularidad)
    numeros_list.append(numero)
    numero = numero + 1
    
    
    
    
#####################################################
colors = {"NEU": 'blue', "NEG": 'red',"POS": 'green'}#array creado para los colores
etiqueta_polaridad = df.FILTRO_2_CLASE_ES.map(colors)#verificamos para poner color por etiqueta
plt.scatter(numeros_list, popularidad_list, color = etiqueta_polaridad)

#popularidadPromedio = (sum(popularidad_list))/(len(popularidad_list))
#popularidadPromedio = "{0:.0f}%".format(popularidadPromedio * 100)
#time  = datetime.now().strftime("A : %H:%M\n El: %m-%d-%y")
#plt.text(0, 1.25, 
 #            "Sentimiento promedio:  " + str(popularidadPromedio) + "\n" + time, 
  #           fontsize=8, 
   #          bbox = dict(facecolor='none', 
    #                     edgecolor='red', 
     #                    boxstyle='square, pad = 1'))
    
######################### PROMEDIOS PARA CADA POLARIDAD
positivo = df.loc[df['FILTRO_2_CLASE_ES']=="POS"]
media_positivo = "{00:.00f}%".format((positivo['FILTRO_2_CLASE_ES'].count() / df['FILTRO_2_CLASE_ES'].count()) * 100)

negativo = df.loc[df['FILTRO_2_CLASE_ES']=="NEG"]
media_negativo = "{00:.00f}%".format((negativo['FILTRO_2_CLASE_ES'].count() / df['FILTRO_2_CLASE_ES'].count()) * 100)

neutro = df.loc[df['FILTRO_2_CLASE_ES']=="NEU"]
media_neutro = "{00:.00f}%".format((neutro['FILTRO_2_CLASE_ES'].count() / df['FILTRO_2_CLASE_ES'].count()) * 100)

##################  TEXTO DE LA GRAFICA
axes = plt.gca()
axes.set_ylim([-1, 2])
plt.text(0, 1.25, 
             "POSITIVOS:  " + str(positivo['FILTRO_2_CLASE_ES'].count()) + " ---  " + str(media_positivo) + 
             "\nNEGATIVOS:  " + str(negativo['FILTRO_2_CLASE_ES'].count()) + " ---  " + str(media_negativo) + 
             "\nNUETROS:  " + str(neutro['FILTRO_2_CLASE_ES'].count()) + " ---  " + str(media_neutro), 
             fontsize=8, 
             bbox = dict(facecolor='none', 
                         edgecolor='red', 
                        boxstyle='square, pad = 1'))
    
      
plt.title('Polaridad del FIAVL del año ' + cabecera)
plt.ylabel('Raggo de polaridad ')
plt.xlabel('Número de Tweets:  ' + str(df['FILTRO_2_CLASE_ES'].count()))
plt.show()