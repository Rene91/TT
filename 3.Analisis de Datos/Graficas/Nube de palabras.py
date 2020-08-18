#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 22:22:09 2020

@author: rene
"""

import matplotlib.pyplot as plt
import pandas as pd
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords


df = pd.read_csv('../../2.LimpiezaDatos/2.filtro_polaridad_clase.csv', sep=';')
df = df.drop(df.columns[[0]], axis='columns') #eliminamos columna


############# FILTRADO POR RANGO
cabeza = "2016-2019"
rango_fecha = (df['FECHA'] >= '2016-01-01') & (df['FECHA'] <= '2021-01-01')
df=df.loc[rango_fecha]



#FILTRADO DE STOPWORDS
def remove_stopwords(texto):
           processed_word_list = []
           texto_aux =""
           texto = texto.split()
           for palabra in texto:
               palabra = palabra.lower() # in case they arenet all lower cased
               if palabra not in stopwords.words("spanish"):
                   texto_aux += palabra +" "
           return texto_aux

cont = 0
texto_list = ""
for ind in df.index:
    #polaridad = str(df['FILTRO_2_CLASE_ES'][ind])#convertimos dato a caden de minusculas
    #if polaridad == 'NEU':
        texto = str(df['FILTRO_1_url_otros'][ind])#convertimos dato a caden de minusculas
        #eliminamos stopwords
        texto = remove_stopwords(texto)
        #####Cargamos tweets
        texto_list += texto#guardar array


from wordcloud import WordCloud
wordcloud = WordCloud(background_color = 'White', colormap = 'Dark2',
                      max_font_size = 150, random_state = 42).generate(texto_list)

plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.title('FIAVL ' + cabeza+ " total " + str(df['FILTRO_2_CLASE_ES'].count()) + " tweets")
plt.show()






