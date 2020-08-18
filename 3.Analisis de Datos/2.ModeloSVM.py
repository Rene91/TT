#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 23:54:31 2020

@author: rene
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# use seaborn plotting defaults
import seaborn as sns; sns.set()


df = pd.read_csv('../2.LimpiezaDatos/2.filtro_polaridad_clase.csv', sep=';')
df = df.drop(df.columns[[0]], axis='columns') #eliminamos columna

############# FILTRADO POR RANGO
cabecera = "2016-2019"
rango_fecha = (df['FECHA'] >= '2016-01-01') & (df['FECHA'] <= '2021-01-01')
df=df.loc[rango_fecha]


##################################################
# Conversion a numeros las etiquetas español
x = df.FILTRO_1_url_otros.astype('str')#comvertimostodos los valores a string
#y = df.FILTRO_2_CLASE_ES.map({'NEG':-1, 'NEU':0, 'POS':1})
y = df.FILTRO_2_CLASE_ES.astype('str')


# Dividir los datos en conjunto de entrenamiento y de test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x , 
                                                    y,
                                                    test_size = 0.8, 
                                                    random_state=1)

print(X_train.shape)
print((X_train.count() / df.FILTRO_2_CLASE_ES.count()) * 100 )

print(X_test.shape)
print((X_test.count() / df.FILTRO_2_CLASE_ES.count()) * 100 )

print(y_train.shape)
print((y_train.count() / df.FILTRO_2_CLASE_ES.count()) * 100 )

print(y_test.shape)
print((y_test.count() / df.FILTRO_2_CLASE_ES.count()) * 100 )

############################## Aplicar BoW para Procesar Nuestros Datos de Pruebas
# Importar el contador de vectorizacion e inicializarlo
from sklearn.feature_extraction.text import CountVectorizer
count_vector = CountVectorizer()

# Fit the training data and then return the matrix
X_training_data = count_vector.fit_transform(X_train)

# Transform testing data and return the matrix. Note we are not fitting the testing data into the CountVectorizer()
X_testing_data = count_vector.transform(X_test)#filas de repeticones


##############################  Implementación SVM con Sci-Kit Learn

from sklearn import svm
#Kernel Lineal
clf = svm.SVC(kernel='linear')
clf.fit(X_training_data, y_train)

Y_predictions = clf.predict(X_testing_data)
print(Y_predictions)
print("rene")
print(clf.predict(count_vector.transform(["sin verlo"])))

############################## Evaluación del modelo
from sklearn.metrics import confusion_matrix    
import seaborn as sns
labels=['NEG', 'NEU' , 'POS']
cm = confusion_matrix(y_test, Y_predictions,labels )#label es la etiqueta de predicion (negativo,neutro,positivo)
print("")
print("############ Resultados del año " +  cabecera + " con " + str(df['FILTRO_2_CLASE_ES'].count()) + " tweets ############")
print("")
print("Matriz Confución")
print(cm)

#######  GRAFICA PARA INTERPRETACIÓN DE MATRIZ DE CONFUCIÓN
fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(False)#quitamos rejillas
cax = ax.matshow(cm)
plt.title('Matriz de confución SVM año ' + cabecera + '\n')
fig.colorbar(cax)
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('True')
for i in range(3):
    for j in range(3):
        ax.text(j, i, cm[i, j], ha='center', va='center', color='green')
plt.show()


fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(cm, annot=True, fmt='d',
xticklabels=category_id_df.Product.values, yticklabels=category_id_df.Product.values)
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()


print("")
print("")
print("Datos clasificados por etiqueta para clasificador SVM")
print(df['FILTRO_2_CLASE_ES'].value_counts())
############################## Evaluación del modelo



print("")
print("")
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
print('Accuracy (Exactitud) score: ', format(accuracy_score(y_test, Y_predictions)))
print('Precision (Precisión) score: ', format(precision_score(y_test, Y_predictions,average='micro')))
print('Recall (sensibilidad) score: ', format(recall_score(y_test, Y_predictions, average='weighted')))
print('F1 score: ', format(f1_score(y_test, Y_predictions, average='weighted')))


