# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 21:18:42 2020

@author: R3gServidor
"""

import pandas as pd##TRABAJAR CON PDF


### METODO PARA EXTRAER TWEETS
ArrayConsulta = [
    
             '23000', 
             '26000', 
             '26668'
            ]


#df= pd.DataFrame()##creacion dataframe interno
fila = []

for consulta in ArrayConsulta:  
    ### LECTURA DEL csv
    datos = pd.read_csv(consulta + '.csv', sep=';')
    aux_df= pd.DataFrame(datos)##creacion dataframe interno
    #df = df.drop(['B', 'E'], axis=1)
    aux_df = aux_df.drop(aux_df.columns[[0]], axis='columns') #eliminamos columna
    fila.append(aux_df)






###creacion de csv
tweets_df = pd.DataFrame(columns=['FILTRO_2_TRADUCCION'])
tweets_df = pd.concat(fila, ignore_index=True)
tweets_df.to_csv('reneRivera.csv', sep=';' , encoding='utf-8-sig')
#df.to_csv('UnionDatos.csv', sep=';' , encoding='utf-8-sig')




### LECTURA DEL csv
datos = pd.read_csv('reneRivera.csv', sep=';')
df1= pd.DataFrame(datos)##creacion dataframe interno
df1 = df1.drop(df1.columns[[0]], axis='columns') #eliminamos columna
traduccion_lis = []
for dato in df1['FILTRO_2_TRADUCCION']: 
        traduccion_lis.append(str(dato))
    
    
    ### LECTURA DEL csv
datos = pd.read_csv('1.filtro_url_#_@_otros33333.csv', sep=';')
df= pd.DataFrame(datos)##creacion dataframe interno
df = df.drop(df.columns[[0]], axis='columns') #eliminamos columna

print(df1)
print(df)
###creacion de csv
df = df.assign(FILTRO_2_TRADUCCION = traduccion_lis) 
df.to_csv('ssssssssssssss.csv', sep=';' , encoding='utf-8-sig')
   
    