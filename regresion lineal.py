import numpy as np

x = [5,15,20,25]
t = [375,487,450,500]
n = len(x)

x = np.array(x)
t = np.array(t)

sumx = sum(x)
sumt = sum(t)
sumx2 = sum(x*x)
sumt2 = sum(t*t)
sumxt = sum(x*t)
promx = sumx/n
promt = sumt/n

b = (sumx*sumt-n*sumxt)/(sumx**2-n*sumx2)
a = promt-b*promx

pronostico = a+b*t
print("Regresión Lineal: ", pronostico)
