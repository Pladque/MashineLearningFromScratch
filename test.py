from func import *
from model import Model
#http://mezeylab.cb.bscb.cornell.edu/labmembers/documents/supplement%205%20-%20multiple%20regression.pdf
#https://medium.com/@lope.ai/multivariate-linear-regression-from-scratch-in-python-5c4f219be6a
with open("student-mat.csv", "r") as f:
    x_train, y_train, x_test, y_test = split_data(f,["G1", "G2"],"G3", 0.1, ';', shuffle = False)


"""print(len(x_train))
print(len(y_train))
print(len(x_test))
print(len(y_test))"""

model = Model(2,1)

model.train(x_train, y_train)
model.test(x_test, y_test, True)

predictions = []

