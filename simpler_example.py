from func import non_int_covariates_to_int, scale, split_data
from model import Model
from time import time
from random import shuffle

covariate_header_indexes = [ "sex", "studytime","failures", "absences", "G1", "G3" ]       #has to have same order as file
response_header = "G2"

if __name__ == '__main__':
    start = time()

    #### setting up the model ###
    amount_of_covariates = len(covariate_header_indexes)
    model = Model(amount_of_covariates, start_weight_value = 1)
    
    ### converting data ###
    with open("student-mat.csv", "r") as f:
        x_train, y_train, x_test, y_test = split_data(
                                            f,covariate_header_indexes,response_header, 
                                            training_size = 0.9, separator = ';', 
                                            shuffle = True, unwanted_sings = ['"']      #change shuffle to true if loading_model
                                            )

    ### converting 'F' and 'M' to 0 and 1
    non_int_covariates_to_int(x_train, "sex", covariate_header_indexes, ["F", "M"])
    non_int_covariates_to_int(x_test, "sex", covariate_header_indexes, ["F", "M"])
    
    ### scaling every value between 0 and 1
    x_test = scale(x_test)
    x_train = scale(x_train)

    ### training model ###
    model.train(x_train, y_train,learing_rate = 0.03,  iterations_number = 5000, 
                skip_side_values = True, mistake_to_skip = 6, 
                interations_b4_skip = 1000, double_learn = True, additional_rand_learn = True)

    ### Printing results ###
    print("avg score ", model.test(x_test, y_test, if_print =True) * 100, "%")
    print("it took ", round(time() - start, 5), "s")       