def train(model, train_covariates, train_response, learing_rate = 0.03, iterations_number = 1000, skip_side_values = False, interations_b4_skip = 5000, mistake_to_skip = 5): # amount_of_learns):          
    cdef float pred_response_and_real_response_diff = 0
    for _ in range(iterations_number):  
        if _ % 1000 == 0:
                print("Iteration number:", _)
        for covariate, response in zip(train_covariates, train_response):
            for x, weight in enumerate(model.weights):
                pred_response_and_real_response_diff = model.diff(response, covariate, model.weights[x])
                if  skip_side_values is False or pred_response_and_real_response_diff <= mistake_to_skip or _  < interations_b4_skip:
                    model.weights[x] -= learing_rate * pred_response_and_real_response_diff
            for x, weight in reversed(list(enumerate(model.weights))):
                pred_response_and_real_response_diff = model.diff(response, covariate, model.weights[x])
                if  skip_side_values is False or pred_response_and_real_response_diff <= mistake_to_skip or _  < interations_b4_skip:
                    model.weights[x] -= learing_rate * pred_response_and_real_response_diff

def diff(respone, covariate, weights):
    return _predict_one(covariate, weights) - respone[0]

def _predict_one(line_covariates, cdef float weights):
    cdef float response = 0
    for x,weight in enumerate(weights):
        if x < len(line_covariates):
            response += weight * line_covariates[x]

    return response + self.weights[-1]
