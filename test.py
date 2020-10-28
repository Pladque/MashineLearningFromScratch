from func import *
from model import Model
#http://mezeylab.cb.bscb.cornell.edu/labmembers/documents/supplement%205%20-%20multiple%20regression.pdf
#https://medium.com/@lope.ai/multivariate-linear-regression-from-scratch-in-python-5c4f219be6a
#https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3049417/

headers_indexes = [ "sex", "studytime","failures", "absences", "G1", "G2" ]       #has to have same order as file
avg_avg_score = 0
for _ in range(10):
    with open("student-mat.csv", "r") as f:
        x_train, y_train, x_test, y_test = split_data(f,headers_indexes,"G3", training_size = 0.9, separator = ';', shuffle = True, unwanted_sings = ['"'])

    non_int_covariates_to_int(x_train, "sex", headers_indexes, ["F", "M"])
    non_int_covariates_to_int(x_test, "sex", headers_indexes, ["F", "M"])

    x_test = scale(x_test)
    x_test = scale(x_test)
    x_train = scale(x_train)
    x_train = scale(x_train)

    model = Model(len(headers_indexes), start_weight_value = 1)

    model.train(x_train, y_train,learing_rate = 0.03,  iterations_number = 5000, 
                skip_side_values = True, mistake_to_skip = 10, interations_b4_skip = 1000)
    print("avg score ", model.test(x_test, y_test, if_print =False, if_round = True, rand_value = 5) * 100, "%")
    avg_avg_score +=model.test(x_test, y_test, if_print =False, if_round = True, rand_value = 5) * 100
print()
print("avg avg score:", avg_avg_score/10)