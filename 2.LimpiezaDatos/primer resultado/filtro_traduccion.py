# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 23:05:33 2020

@author: R3g Systems
"""


import os
#os.system("pip install pandas")


import pandas as pd##trabaja con PDF
import requests  ##carga la URL

############################### CREACION DE ARREGLO YA TRADUCIDO  #################################

# METODO PARA TRADUCIR TEXTO
def Traduccion(source, target, text):
	parametros = {'sl': source, 'tl': target, 'q': text}
	cabeceras = {"Charset":"UTF-8","User-Agent":"AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1"}
	url = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=es-ES&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"
	response = requests.post(url, data=parametros, headers=cabeceras)
	if response.status_code == 200:
		for x in response.json()['sentences']:
			return x['trans']
	else:
		return "Ocurrió un error"
    

### LECTURA DEL csv
datos = pd.read_csv('1.filtro_url_#_@_otros.csv', sep=';')
df= pd.DataFrame(datos)##creacion dataframe interno
df = df.drop(df.columns[[0]], axis='columns') #eliminamos columna


##traduccion texto, subjetividad y poloaridad
traduccion_lis = []

cont = 0
for dato in df['FILTRO_1_url_otros']: 
    cont = cont + 1
    if(cont > 23000 ):
        traduccion = Traduccion("es", "en", str(dato).replace('|' , ' '))
        print(str(cont) + " ->   " + traduccion)
    
        ######## carga de listas con su respectiva variable
        traduccion_lis.append(traduccion)
        #if(cont % 1000 == 0 ):
            #df1= pd.DataFrame()##creacion dataframe interno
            #df1 = df1.assign(FILTRO_2_TRADUCCION = traduccion_lis)
            #df1.to_csv(str(cont) + '.csv', sep=';' , encoding='utf-8-sig')
    

###creacion de nuevas colunas
df = df.assign(FILTRO_2_TRADUCCION = traduccion_lis)

###creacion de csv
df.to_csv('2.filtro_traduccion.csv', sep=';' , encoding='utf-8-sig')
   
    