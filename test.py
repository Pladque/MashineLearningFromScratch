from func import *
from model import Model

f = open("student-mat.csv", "r")

#plan dzialania:
#biore 2 punkty i obliczam wsplolczynniki (jak do wykresu)
#https://medium.com/deep-math-machine-learning-ai/chapter-1-complete-linear-regression-with-math-25b2639dde23
#https://medium.com/towards-artificial-intelligence/understanding-the-simple-maths-behind-simple-linear-regression-3ce4a30e7602

x_train, y_train, x_test, y_test = split_data(f,["G1", "G2"],"G3", 0.1, ';')

print(x_train[0])
print(y_train[0])
print(x_test[0])
print(y_test[0])

model = Model(2,0)

predictions = []

