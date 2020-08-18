#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 00:20:27 2020

@author: rene
"""


import pandas as pd##TRABAJAR CON PDF


########################### MÉTODO PARA UNIR TODO LOS CSV
ArrayConsulta = [
            'Festival de Artes Vivas en Loja',
            '@festivaloffloja','@FestivalDeLoja',
            '#FIAVL','#FIAVL2016', '#FIAVL2017' ,'#FIAVL2018', '#FIAVL2019', '#FIAVL2020', 
            '#MiMejorMomentoFIAV', '#MiMejorMomentoFIAV2016', '#MiMejorMomentoFIAV2017', '#MiMejorMomentoFIAV2018', '#MiMejorMomentoFIAV2019', '#MiMejorMomentoFIAV2020',
            '#artesvivas', 
             '#FestivalLojaMasTuyoQueNunca',
             '#OFFLoja', 
             '#ElArteViveEnLoja'
            ]



fila = []
### UNIÓN DE CSV RECOPILADOS DE TWEETER
for consulta in ArrayConsulta:  
    ### LECTURA DEL csv
    print(consulta)
    datos = pd.read_csv('../1.DescargaTwees/' + consulta + '.csv', sep=';')
    aux_df= pd.DataFrame(datos)##creacion dataframe interno 
    aux_df = aux_df.drop(aux_df.columns[[0]], axis='columns') #eliminamos columna 0
    fila.append(aux_df)



###creacion de csv
tweets_df = pd.DataFrame(columns=['ID', 'ENLACE', 'USUARIO', '@CUENTA', 'FECHA', 'RETWEETS', 'FAVORITO','MENCIONA', 'HASHTAGS', 'GEO','TEXTO'])
tweets_df = pd.concat(fila, ignore_index=True)
tweets_df.to_csv('0.UnionDatos.csv', sep=';' , encoding='utf-8-sig')
#tweets_df.to_csv("Original_" + str(cont) +".csv", sep=';' , encoding='utf-8-sig')