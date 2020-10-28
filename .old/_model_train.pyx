def train(model, train_covariates, train_response, learing_rate = 0.03, iterations_number = 1000, skip_side_values = False, interations_b4_skip = 5000, mistake_to_skip = 5): # amount_of_learns):          
    cdef float pred_response_and_real_response_diff = 0
    cdef float pred_response = 0

    for _ in range(iterations_number):  
        if _ % 1000 == 0:
                print("Iteration number:", _)
        for covariate, response in zip(train_covariates, train_response):
            for x, weight in enumerate(model.weights):
                if  skip_side_values is False or pred_response_and_real_response_diff <= mistake_to_skip or _  < interations_b4_skip:
                    pred_response = 0
                    for x,weight in enumerate(model.weights[x]):
                        if x < len(covariate):
                            pred_response += weight * covariate[x]        
                    model.weights[x] -= learing_rate * (pred_response - response[0])
            for x, weight in reversed(list(enumerate(model.weights))):
                if  skip_side_values is False or pred_response_and_real_response_diff <= mistake_to_skip or _  < interations_b4_skip:
                    pred_response = 0
                    for x,weight in enumerate(model.weights[x]):
                        if x < len(covariate):
                            pred_response += weight * covariate[x]        
                    model.weights[x] -= learing_rate * (pred_response - response[0])
    return model

