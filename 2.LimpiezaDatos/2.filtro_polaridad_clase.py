# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 03:18:42 2020

@author: R3gServidor
"""

import os
#os.system("pip install sentiment-analysis-spanish")
#os.system("pip install keras tensorflow")
import pandas as pd##TRABAJAR CON PDF
from textblob import TextBlob
#from textblob.sentiments import NaiveBayesAnalyzer
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer#polaridad textos en español



### lectura de csv
datos = pd.read_csv('1.filtro_url_#_@_otros.csv', sep=';')
df= pd.DataFrame(datos)##creación dataframe interno
df = df.drop(df.columns[[0]], axis='columns') #eliminamos columna

# creacón de array para cargar datos
polaridad_es_list = []
clase_ES_list = []
cont = 0

# Creación de polaridad y las etiquetas POSITIVO, NEGATIVO y NETRO en Español
for dato in df.index:
    
    ####### polaridad en español
    tweet_es = str(df['FILTRO_1_url_otros'][dato]) #obtención de tweet
    polaridad_es = SentimentIntensityAnalyzer().polarity_scores(tweet_es)#obtenemos sentimiento
    polaridad_es = polaridad_es['compound']#obtenemos de dato de polaridad
    
    ######## carga de lista con su respectiva variable    
    polaridad_es_list.append(polaridad_es)
    
    #### CLASE PARA POLARIDADEN ESPAÑOL######
    if polaridad_es < 0.0:
        clase_ES_list.append("NEG")#clase negativa
    elif polaridad_es > 0.0:
        clase_ES_list.append("POS")#clase positiva
    else:
          clase_ES_list.append("NEU")#clase neutra
    cont = cont + 1
    print(cont)
    
###creacion de csv
df = df.assign(FILTRO_2_POLARIDAD_ES = polaridad_es_list) 
df = df.assign(FILTRO_2_CLASE_ES = clase_ES_list) 
#df.to_csv('2.filtro_polaridad_clase.csv', sep=';' , encoding='utf-8-sig')