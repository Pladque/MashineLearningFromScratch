from func import non_int_covariates_to_int, scale, split_data, load_model, save_model
from model import Model
from time import time
from random import shuffle
import sys

#to add:
# cython
# documentation

covariate_header_indexes = [ "sex", "studytime","failures", "absences", "G1", "G2" ]       #has to have same order as file
response_header = "G3"

LOAD_MODEL = False
SAVE_MODEL = False
AMOUNT_OF_LEARNS = 1  #how many times will you let model learns, weights from best results will be saved

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

    non_int_covariates_to_int(x_train, "sex", covariate_header_indexes, ["F", "M"])
    non_int_covariates_to_int(x_test, "sex", covariate_header_indexes, ["F", "M"])
    
    x_test = scale(x_test)
    x_train = scale(x_train)

    ### Loading model or training it ###
    if LOAD_MODEL:
        if load_model(model) is False:  
            sys.exit("LOAD ERROR. PROGRAM STOPPED")
    else:
        best = 0
        model = Model(amount_of_covariates, start_weight_value = 1)
        for _ in range(AMOUNT_OF_LEARNS):
            print("#", _)
            ### randomizing order in data ###
            lines_train = list(zip(x_train, y_train))
            lines_test = list(zip(x_test, y_test))
            shuffle(lines_train)
            shuffle(lines_test)
            x_train, y_train= zip(*lines_train)
            x_test, y_test = zip(*lines_test)

            model.train(x_train, y_train,learing_rate = 0.03,  iterations_number = 5000, 
                        skip_side_values = False, mistake_to_skip = 10, 
                        interations_b4_skip = 1000, double_learn = False, add_rand_learn = False)
            print("LOOP DONE")
            if model.test(x_test, y_test, if_print =False, if_round = False, rand_value = 0) > best:
                best = model.test(x_test, y_test, if_print =False, if_round = False, rand_value = 0)
                ### Saving model ###
                if SAVE_MODEL:
                    save_model(model)       #saving model on progress in case of lack of power

    ### Printing (best) results ###
    print()
    print("avg score ", model.test(x_test, y_test, if_print =True, 
            if_round = False, rand_value = 0, min = 0, max = 20) * 100, "%")
    print("it took ", round(time() - start, 5), "s")       