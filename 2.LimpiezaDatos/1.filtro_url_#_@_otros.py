# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 00:10:25 2020

@author: R3gServidor
"""

import os
#os.system("re")
#os.system("pip install nltk")
import re, string
import pandas as pd##TRABAJAR CON PDF
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
#os.system("pip install hunspell")
import hunspell#PARA CORREGIR DATOS



#################################### METODOS A UTILIZAR  ############
# FILTRADO DE MENCIONES Y HASHTAG
def filtrado(texto, filtro):#filtro puede ser Hashtag o Mencion
    texto = str(texto).lower()
    filtro = filtro.split()
    for f in filtro:
        texto = texto.replace(str(f).lower(), "")#quitamos hashtag
    return texto

        
### CORRECIÓN DE PALABRAS MAL ESCRITAS EN ESPAÑOL
def corregir_palabras(palabras):  
    diccionario = hunspell.HunSpell('/usr/share/hunspell/es_EC.dic', 
                                    '/usr/share/hunspell/es_EC.aff')# obtenemos la codificacion del idioma Ecuador

    # autocorrección de palabras
    corregida =""
    for p in palabras:
        ok = diccionario.spell(p)   # verificamos ortografia
        if not ok:
            sugerencias = diccionario.suggest(p)
            if len(sugerencias) > 0:  # hay sugerencias
                # tomamos la  mejor sugerencia(decodificada a string)
                mejor_sugerencia = sugerencias[0]   
                corregida += mejor_sugerencia + " "
            else:
                corregida += p + " " # no hay ninguna sugerecia para la palabra
        else:
            corregida += p  + " "  # esta palabra esta corregida

    return corregida




### LECTURA DEL csv
datos = pd.read_csv('0.UnionDatos.csv', sep=';')
df= pd.DataFrame(datos)##creacion dataframe interno
df = df.drop_duplicates('ENLACE')#eliminación de tweest duplicados   F
df = df.drop(df.columns[[0]], axis='columns') #eliminamos columna

cont = 0
columna = []
for ind in df.index:
    texto = str(df['TEXTO'][ind])#convertimos dato a cadena
    
    hashtag = str(df['HASHTAGS'][ind])#convertimos dato a cadena 
    texto = filtrado(texto, hashtag)#quitamos Hashtag
    
    mencion = str(df['MENCIONA'][ind])#convertimos dato a cadena
    texto = filtrado(texto, mencion)#quitamos Mencion
    
    #eliminar url
    texto = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', texto)
    
    #eliminar expresiones regulares    
    texto = re.sub('['+string.punctuation+']', '', texto)
    
    ### corrección de palabras mal escritas
    texto =  corregir_palabras(texto.split())
        
    #####Cargamos tweets
    columna.append(texto)#guardar array
    cont +=1
    print(cont)
    
    

###creacion de csv
df = df.assign(FILTRO_1_url_otros = columna) 
df.to_csv('1.filtro_url_#_@_otros.csv', sep=';' , encoding='utf-8-sig')


        