# Comandos para instalar la paqueteria necesaria:
#    pip install numpy
#    pip install scipy
#    python -mpip install -U matplotlib
#    python -mpip install -U sklearn
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import numpy as np
import random as rn  

vinos = datasets.load_wine()

datos = vinos.data
#Esta base de datos contiene doce caracteristicas o solo necesitamos 3
#la variable caracteristicas está guardando 178 datos a diferencia de
#la base de datos de Julia que solo contiene 135
caracteristicas = list(map(lambda x: [x[0], x[6], x[11]], datos))
#tipo_de_vino solo contiene ceros, unos y dos. Otra diferencia de esta BD
#es que la BD de julia tiene sus rangos (1,2,3) iguales mientras que  esta
#base de datos no, se especifican los rangos en los comentarios de variables
#vino_aleat_1,2,3
tipo_de_vino = vinos.target



#Se crean listas con valores aleatorios en un rango definido
#es decir el rango que haya entre cada tipo de vino tomando el 85% de cada rango
#como si cada uno fuera el 100%
vino_1_aleat = rn.sample(range(0,59),k = 59)#85%=50    15%=9
vino_2_aleat = rn.sample(range(60,131),k = 71)#85%=60  15%=11
vino_3_aleat = rn.sample(range(132,178),k = 46)#85%=39   15% =7

#En julia, los ciclos que están a continuación se hacen con instrucciones mas simples
# Se trata de a partir de los indices aleatorios que generamos anteriormente
#tomar esa cantidad de valores de la matris caracteristicas y de ese modo graficar con
#valores aleatorios del 85% de los totales
#__________________________________________________________________________________
x_entren = []
x_entren1 = []
x_entren2 = []
x_entren3  = []
for i in vino_1_aleat[0:50]:
    x_entren1.append(caracteristicas[i][0])

for i in vino_2_aleat[0:60]:
    x_entren1.append(caracteristicas[i][0])
    
for i in vino_3_aleat[0:39]:
    x_entren1.append(caracteristicas[i][0])

#_____________________________________________
for i in vino_1_aleat[0:50]:
    x_entren2.append(caracteristicas[i][1])

for i in vino_2_aleat[0:60]:
    x_entren2.append(caracteristicas[i][1])
    
for i in vino_3_aleat[0:39]:
    x_entren2.append(caracteristicas[i][1])

#____________________________________________

for i in vino_1_aleat[0:50]:
    x_entren3.append(caracteristicas[i][2])

for i in vino_2_aleat[0:60]:
    x_entren3.append(caracteristicas[i][2])
    
for i in vino_3_aleat[0:39]:
    x_entren3.append(caracteristicas[i][2])

x_entren = [x_entren1,x_entren2,x_entren3]
y_entren = []
#y_entren se llena con los tipos de vino
#considerando los rangos que ya sabemos
y_entren.extend(tipo_de_vino[0:50])
y_entren.extend(tipo_de_vino[60:120])
y_entren.extend(tipo_de_vino[132:171])
#x_prueba y y_prueba se llenan con caracteristicas y tipos restantes, es decir, el 15& de los datos
#______________________________________________________________________
x_prueba = []
x_prueba1 = []
x_prueba2 = []
x_prueba3  = []
for i in vino_1_aleat[51:59]:
    x_prueba1.append(caracteristicas[i][0])

for i in vino_2_aleat[61:71]:
    x_prueba1.append(caracteristicas[i][0])
    
for i in vino_3_aleat[40:46]:
    x_prueba1.append(caracteristicas[i][0])

#_____________________________________________
for i in vino_1_aleat[51:59]:
    x_prueba2.append(caracteristicas[i][1])

for i in vino_2_aleat[61:71]:
    x_prueba2.append(caracteristicas[i][1])
    
for i in vino_3_aleat[40:46]:
    x_prueba2.append(caracteristicas[i][1])

#____________________________________________

for i in vino_1_aleat[51:59]:
    x_prueba3.append(caracteristicas[i][2])

for i in vino_2_aleat[61:71]:
    x_prueba3.append(caracteristicas[i][2])
    
for i in vino_3_aleat[40:46]:
    x_prueba3.append(caracteristicas[i][2])

x_prueba = [x_prueba,x_prueba2,x_prueba3]
y_prueba = []
y_prueba.extend(tipo_de_vino[51:59])
y_prueba.extend(tipo_de_vino[61:71])
y_prueba.extend(tipo_de_vino[40:46])



#Se grafica con los datos de entrenamiento
fig = plt.figure(1)
ax = Axes3D(fig)
ax.scatter(x_entren[0][0:49],x_entren[1][0:49],x_entren[2][0:49],color = "b")
ax.scatter(list(x_entren[0][50:109]),list(x_entren[1][50:109]),list(x_entren[2][50:109]),color = "r")
ax.scatter(list(x_entren[0][110:149]),list(x_entren[1][110:149]),list(x_entren[2][110:149]),color = "g")
ax.set_xlabel("Contenido de alcohol")
ax.set_ylabel("Contenido de flavonoides")
ax.set_zlabel("Densidad optica relativa")
plt.show()


#Se busca obtener la resta entre los datos de entrenamiento y sus promedios de cada tipo
#para despues hacer un array con los promedio generales de los tipos en x_entren
x_entren1 = x_entren[0][:]-np.mean(x_entren[0][:])
x_entren2 = x_entren[1][:]-np.mean(x_entren[1][:])
x_entren3 = x_entren[2][:]-np.mean(x_entren[2][:])
x_entren = [x_entren1,x_entren2,x_entren3]
#Se busca obtener matrices de valores promedio de x_entren para poder centrar en 0 las caracteristicas
prom_1 = [np.mean(x_entren[0][0:50]),np.mean(x_entren[1][0:50]),np.mean(x_entren[2][0:50])]
prom_2 =  [np.mean(x_entren[0][51:110]),np.mean(x_entren[1][51:110]),np.mean(x_entren[2][51:110])]
prom_3 =  [np.mean(x_entren[0][111:149]),np.mean(x_entren[1][111:149]),np.mean(x_entren[2][111:149])]

#Se grafica ya con los datos centrados en 0 y poniendo un Punto centralizado en el promedio de cada tipo
fig = plt.figure(2)
ax = Axes3D(fig)
ax.scatter(x_entren[0][0:49],x_entren[1][0:49],x_entren[2][0:49],color = "b")
ax.scatter(prom_1[0],prom_1[1],prom_1[2],s = 100,color = "b")
ax.scatter(x_entren[0][50:109],x_entren[1][50:109],x_entren[2][50:109],color = "r")
ax.scatter(prom_2[0],prom_2[1],prom_2[2],s = 100,color = "r")
ax.scatter(x_entren[0][111:149],x_entren[1][111:149],x_entren[2][111:149],color = "g")
ax.scatter(prom_3[0],prom_3[1],prom_3[2],s = 100,color = "g")
ax.set_xlabel("Contenido de alcohol")
ax.set_ylabel("Contenido de flavonoides")
ax.set_zlabel("Densidad optica relativa")
plt.show()


#El array W claramente solo está reuniciendo los 3 valores promedio de las caracteristicas de alcohol
W = [prom_1,prom_2,prom_3]
#
#v1 Obtiene el prodcucto punto e W y x_entren
v1 = np.dot(W,x_entren)

#v reune los elementos de las 3 columnas de v1 para hubicarlas en un solo arreglo 
v = []
v.extend(v1[0])
v.extend(v1[1])
v.extend(v1[2])
#v_max obtiene datos maximos (no negativos)

v_max = list(filter(lambda x:x>=0,v))

#v_max_ind obtiene los indices de esos datos positivos tomando como referencia el array v
v_max_ind1 = []

i = 0
while i <= len(v)-1:
    if v[i]>= 0:
        v_max_ind1.append(i)
    i = i+1
#Se supone que esta instruccion debió de crear una matriz que solo deberia contener 0,1 y 2
#Pero debido a la cantidad de datos, a que no son del mismo tamaño los tipos, o no sé
#No salió esta instruccion como se esperaba y por lo tanto lo demás tampoco resultará
v_max_ind = np.subtract(v_max_ind1,list(range(0,len(v_max_ind1)*3,3)))

