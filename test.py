from func import *
f = open("student-mat.csv", "r")



x_train, y_train, x_test, y_test = split_data(f,["G1", "G2"],"G3", 0.1, ';')
#testuj to jezcze mby
print(x_train[0])
print(y_train[0])
print(x_test[0])
print(y_test[0])