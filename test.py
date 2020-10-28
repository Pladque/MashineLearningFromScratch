from func import *
from model import Model
from config import *
import time

covariate_header_indexes = [ "sex", "studytime","failures", "absences", "G1", "G2" ]       #has to have same order as file
response_header = "G3"

if __name__ == '__main__':
    start = time.time()
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

    amount_of_covariates = len(covariate_header_indexes)
    model = Model(amount_of_covariates, start_weight_value = 1)

    model.train(x_train, y_train,learing_rate = LEARNING_RATE,  iterations_number = ITERATIONS_NUMBER, 
                skip_side_values = SKIP_SIDE_VALUES, mistake_to_skip = MISTAKE_TO_SKIP, 
                interations_b4_skip = NUMBER_OF_ITERATION_BEFORE_FIRST_SKIP)

    print("avg score ", model.test(x_test, y_test, if_print =False, 
            if_round = ROUND_TEST_RESPONSE, rand_value = ROUND_NDIGIDTS) * 100, "%")
    print("it took ", time.time() - start)
        