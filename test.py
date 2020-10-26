from func import *
from model import Model
#http://mezeylab.cb.bscb.cornell.edu/labmembers/documents/supplement%205%20-%20multiple%20regression.pdf
#https://medium.com/@lope.ai/multivariate-linear-regression-from-scratch-in-python-5c4f219be6a
#https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3049417/

headers_indexes = ["studytime","absences", "G1", "G2" ]       #fix it later, bc now it has to be in same order as it is in file if i want to convert non intvalues to inst by my own function
with open("student-mat.csv", "r") as f:
    x_train, y_train, x_test, y_test = split_data(f,headers_indexes,"G3", training_size = 0.6, separator = ';', shuffle = True)


"""print(len(x_train))
print(len(y_train))
print(len(x_test))
print(len(y_test))"""

#non_int_covariates_to_int(x_train, "sex", headers_indexes, ["F", "M"]) #change this func bc now it returns ints as
#non_int_covariates_to_int(x_test, "sex", headers_indexes, ["F", "M"]) #change this func bc now it returns ints as

model = Model(len(headers_indexes), start_weight_value = 1)

model.train(x_train, y_train,learing_rate = 0.0001,  iterations_number = 50000)
print("avg score ", model.test(x_test, y_test, if_print =True, if_round = True, rand_value = 0), "%")

predictions = []