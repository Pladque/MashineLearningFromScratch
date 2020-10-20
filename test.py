from func import *
from model import Model

f = open("student-mat.csv", "r")

#plan dzialania:
#Zmien nazwy z input i autput na ... *jest w filmiku o linear regresion XD)
#biore 2 punkty i obliczam wsplolczynniki (jak do wykresu)
#https://medium.com/deep-math-machine-learning-ai/chapter-1-complete-linear-regression-with-math-25b2639dde23
#https://medium.com/towards-artificial-intelligence/understanding-the-simple-maths-behind-simple-linear-regression-3ce4a30e7602

x_train, y_train, x_test, y_test = split_data(f,["G1", "G2"],"G3", 0.1, ';')

"""print(len(x_train))
print(len(y_train))
print(len(x_test))
print(len(y_test))"""

model = Model(2,1)

model.train(x_train, y_train)
model.test(x_test, y_test)

predictions = []

