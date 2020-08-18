# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:44:12 2020

@author: R3gServidor
"""



import os
#os.system("pip install TextBlob")
#os.system("pip install GetOldTweets3")
#os.system("pip install pandas")
#os.system("pip install senborn")

from textblob import TextBlob ##analisis de sentimientos
import GetOldTweets3 as got  ##EXTRAE LOS TWEETS
from datetime import datetime, timedelta ##EXTRAE FECHAS
import pandas as pd##TRABAJAR CON PDF





#############  EXTRACCIÓN DE TWEETS POR PARAMETRO DE BUSQUEDA  ############################

## ARRAY DE CONSULTA DE TWEETS
ArrayConsulta = [    
            'Festival de Artes Vivas en Loja',
            '@festivaloffloja','@FestivalDeLoja',
            '#FIAVL','#FIAVL2016', '#FIAVL2017' ,'#FIAVL2018', '#FIAVL2019', '#FIAVL2020', 
            '#MiMejorMomentoFIAV', '#MiMejorMomentoFIAV2016', '#MiMejorMomentoFIAV2017', '#MiMejorMomentoFIAV2018', '#MiMejorMomentoFIAV2019', '#MiMejorMomentoFIAV2020',
            '#artesvivas', 
             '#FestivalLojaMasTuyoQueNunca',
             '#OFFLoja', 
             '#OffLoja', '#ElArteViveEnLoja'
            ]


fecha_inicio = '2015-12-28'
fecha_final = '2020-02-20'

### METODO PARA EXTRAER TWEETS
for consulta in ArrayConsulta:
    print('')
    print('')
    print('Palabara Busqueda:  ' + consulta)
    fila = []
    # Creation of query object
    tweetCriterio = (
                        got.manager.TweetCriteria().
                        setQuerySearch(consulta).
                        setSince(fecha_inicio).
                        setUntil(fecha_final)
                        #setMaxTweets(count)
                    )
    
    tweets = got.manager.TweetManager.getTweets(tweetCriterio)
    
    cont = 0
    for tweet in tweets:
        cont = cont + 1  
        fila += [   
                    [
                        tweet.id,
                        tweet.permalink,
                        tweet.username,
                        tweet.to,
                        tweet.date,
                        tweet.retweets,
                        tweet.favorites,
                        tweet.mentions,
                        tweet.hashtags,
                        tweet.geo,
                        tweet.text
                    ]                         
                ]    
    print('Toatal datos:  ' + consulta)
    tweets_df = pd.DataFrame(fila, columns=['ID', 'ENLACE', 'USUARIO', '@CUENTA', 'FECHA', 'RETWEETS', 'FAVORITO','MENCIONA', 'HASHTAGS', 'GEO','TEXTO'])
    tweets_df.to_csv(consulta + '.csv', sep=';' , encoding='utf-8-sig')