from random import randint
from libcpp cimport bool

def train(model, train_covariates, train_response, float learing_rate = 0.03, int iterations_number = 1000, bool skip_side_values = False,
         int interations_b4_skip = 5000, float mistake_to_skip = 5, bool double_learn = False, bool add_rand_learn = False):  # amount_of_learns):          
    cdef float pred_response_and_real_response_diff
    for _ in range(iterations_number):  
        if _ % 1000 == 0:
                print("Iteration:", _)
        for covariate, response in zip(train_covariates, train_response):
            for x in range(len(model.weights)):
                pred_response_and_real_response_diff = diff(model, response, covariate)
                if  skip_side_values is False or pred_response_and_real_response_diff <= mistake_to_skip or _  < interations_b4_skip:
                    model.weights[x] -= learing_rate * pred_response_and_real_response_diff
            if double_learn:
                for x in reversed(range(len(model.weights))):
                    pred_response_and_real_response_diff = diff(model, response, covariate)
                    if  skip_side_values is False or pred_response_and_real_response_diff <= mistake_to_skip or _  < interations_b4_skip:
                        model.weights[x] -= learing_rate * pred_response_and_real_response_diff
            if add_rand_learn:
                pred_response_and_real_response_diff = diff(model, response, covariate)
                if  skip_side_values is False or pred_response_and_real_response_diff <= mistake_to_skip or _  < interations_b4_skip:
                    rand = randint(0, len(model.weights)-1)
                    model.weights[rand] -= learing_rate * pred_response_and_real_response_diff


cdef float diff(model, float[] response, covariate):
    cdef float real_response = response[0]
    return _predict_one(model, covariate) - real_response

cdef float _predict_one(model, line_covariates):
    cdef float response = 0
    for x,weight in enumerate(model.weights):
        if x < len(line_covariates):
            response += weight * line_covariates[x]

    return response + model.weights[-1]