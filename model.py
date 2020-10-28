class Model:

    def __init__(self,inputs_number, start_weight_value):
        self.weights = []   #chyba bd potrzebowal inputs_number+1 zeby miec wykres dobry(w[0]+w[1]*x[0]+w[2]*x[1] itd..)
        for _ in range(inputs_number):
            self.weights.append(start_weight_value)
        self.weights.append(start_weight_value)      #just for test


    def diff(self, respone, covariate):
        return self._predict_one(covariate) - respone[0]


    def train(self, train_covariates, train_response, learing_rate = 0.03, iterations_number = 1000, skip_side_values = False, interations_b4_skip = 5000, mistake_to_skip = 5): # amount_of_learns):          
        for _ in range(iterations_number):  
            if _ % 1000 == 0:
                    print("Iteration number:", _)
            for covariate, response in zip(train_covariates, train_response):
                for x, weight in enumerate(self.weights):
                    pred_response_and_real_response_diff = self.diff(response, covariate)
                    if  skip_side_values is False or pred_response_and_real_response_diff <= mistake_to_skip or _  < interations_b4_skip:
                        self.weights[x] -= learing_rate * pred_response_and_real_response_diff
                for x, weight in reversed(list(enumerate(self.weights))):
                    pred_response_and_real_response_diff = self.diff(response, covariate)
                    if  skip_side_values is False or pred_response_and_real_response_diff <= mistake_to_skip or _  < interations_b4_skip:
                        self.weights[x] -= learing_rate * pred_response_and_real_response_diff
                    
    

    def test(self,test_covariates, test_response, if_print = False, if_round = False, rand_value = 0):
        average_mistake = 0
        for test_input, test_output in zip(test_covariates,test_response):
            average_mistake += self._print_predicted_values(test_input, test_output, if_print, if_round, rand_value)
        if if_print:
            for x, weight in enumerate(self.weights):
                print(x,". weight: ",weight)

        return average_mistake/ len(test_response)
         
    def predict(self, covariates, if_round = False, rand_value = 0): #returns prediction, its for predicting only one table with covariates
        response = 0
        for x, weight in enumerate(self.weights):
            if x < len(covariates):
                response += weight * covariates[x]
        response += self.weights[-1]        #last element in list a constant term

        if if_round:
            response = round(response,rand_value) 
        return [response]

    def _predict_one(self, line_covariates):
        response = 0
        for x,weight in enumerate(self.weights):
            if x < len(line_covariates):
                response += weight * line_covariates[x]

        return response + self.weights[-1]

    def _print_predicted_values(self, test_input, test_output, if_print, if_round, rand_value):
        mistake = abs(self.predict(test_input, if_round, rand_value)[0]-test_output[0])
        if if_print:
            print("PREDICTED: ",self.predict(test_input, if_round, rand_value)," ACTUAL: ", test_output, 
                    "COVARIATES: ",test_input,
                    "MISTAKE: ", mistake,'points; ', 
                    )
        if test_output[0] != 0:
            return 1 - (mistake / test_output[0])
        elif (self.predict(test_input, if_round, rand_value)[0]) != 0:
            return 1 - (mistake / (self.predict(test_input, if_round, rand_value)[0]))
        else:
            return 0


    ### OLD TRAIN ###
    """#idk if i need this
        average_cowariates = []
        average_response = 0
        ###
        for _ in range(len(train_covariates[0])):
            average_cowariates.append(0)
        
        for i, covariates in enumerate(train_covariates):
            for x, covariate in enumerate(covariates):
                average_cowariates[x] += covariate
        
        for _train_response in train_response:
            average_response += _train_response[0]

        for x, covariate in enumerate(average_cowariates):
            average_cowariates[x] = covariate / len(train_covariates)

        average_response = average_response / len(train_response) """

    """print(average_cowariates[0])
        print(average_cowariates[1])
        print(average_response) #:)
        ingredient = []

        for i, covariates in enumerate(train_covariates):
            ingredient.append([])
            for x, covariate in enumerate(covariates):
                ingredient[i].append(covariate - average_cowariates[x])
            ingredient[i].append(train_response[i][0] -  average_response)  
        
        print(ingredient)"""
