from func import *
from model import Model
from config import *
#http://mezeylab.cb.bscb.cornell.edu/labmembers/documents/supplement%205%20-%20multiple%20regression.pdf
#https://medium.com/@lope.ai/multivariate-linear-regression-from-scratch-in-python-5c4f219be6a
#https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3049417/

covariate_header_indexes = [ "sex", "studytime","failures", "absences", "G1", "G2" ]       #has to have same order as file
response_header = "G3"

with open("student-mat.csv", "r") as f:
    x_train, y_train, x_test, y_test = split_data(
                                        f,covariate_header_indexes,response_header, 
                                        training_size = TRAINING_SIZE, separator = ';', 
                                        shuffle = SHUFFLE, unwanted_sings = ['"']
                                        )

non_int_covariates_to_int(x_train, "sex", covariate_header_indexes, ["F", "M"])
non_int_covariates_to_int(x_test, "sex", covariate_header_indexes, ["F", "M"])

x_test = scale(x_test)
x_train = scale(x_train)

covariates_number = len(covariate_header_indexes)
model = Model(covariates_number, start_weight_value = 1)

model.train(x_train, y_train,learing_rate = LEARNING_RATE,  iterations_number = ITERATIONS_NUMBER, 
            skip_side_values = SKIP_SIDE_VALUES, mistake_to_skip = MISTAKE_TO_SKIP, 
            interations_b4_skip = NUMBER_OF_ITERATION_BEFORE_FIRST_SKIP)

print("avg score ", model.test(x_test, y_test, if_print =False, 
        if_round = ROUND_TEST_RESPONSE, rand_value = ROUND_NDIGIDTS) * 100, "%")
    