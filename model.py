import pyximport; pyximport.install
import model_train

from random import randint

class Model:

    def __init__(self,inputs_number, start_weight_value, weights = []):
        self.weights = []   #chyba bd potrzebowal inputs_number+1 zeby miec wykres dobry(w[0]+w[1]*x[0]+w[2]*x[1] itd..)
        for _ in range(inputs_number + 1):
            self.weights.append(start_weight_value)



    def train(self, train_covariates, train_response, learing_rate = 0.03, iterations_number = 1000, skip_side_values = False, 
                        interations_b4_skip = 5000, mistake_to_skip = 5, double_learn = False, additional_rand_learn = False):          
        model_train.train(self, train_covariates, train_response, learing_rate, iterations_number, 
                            skip_side_values, interations_b4_skip, mistake_to_skip, double_learn, additional_rand_learn)

        
        

    def test(self,test_covariates, test_response, if_print = False, if_round = False, rand_value = 0, min = float('-inf'), max = float('inf')):
        average_mistake = 0
        for test_input, test_output in zip(test_covariates,test_response):
            average_mistake += self._predict_and_print_predicted_values(test_input, test_output, if_print, if_round, rand_value, min, max)
        if if_print:
            for x, weight in enumerate(self.weights):
                print(x,". weight: ",weight)
        print()
        return average_mistake/ len(test_response)
         
    def predict(self, covariates, if_round = False, rand_value = 0, min = float('-inf'), max = float('inf')): #returns prediction, its for predicting only one table with covariates
        response = 0
        for x, weight in enumerate(self.weights):
            if x < len(covariates):
                response += weight * covariates[x]
        response += self.weights[-1]        #last element in list a constant term

        if response < min: response = min
        elif response > max: response = max

        if if_round:
            response = round(response,rand_value) 
        return [response]


    def _predict_and_print_predicted_values(self, covariates, response, if_print, if_round, rand_value, min = float('-inf'), max = float('inf')):
        mistake = abs(self.predict(covariates, if_round, rand_value, min, max)[0]-response[0])
        if if_print:
            print("PREDICTED: ",self.predict(covariates, if_round, rand_value, min, max)," ACTUAL: ", response, 
                    "COVARIATES: ",covariates,
                    "MISTAKE: ", mistake,'points; ', 
                    )
        if response[0] != 0:
            return abs(1 - (mistake / response[0]))
        elif (self.predict(covariates, if_round, rand_value)[0]) != 0:
            return abs(1 - (mistake / (self.predict(covariates, if_round, rand_value)[0])))
        else:
            return 0

    def load_weights(self, weights):
        self.weights = weights

    ### old ###
    def _predict_one(self, line_covariates):
        response = 0
        for x,weight in enumerate(self.weights):
            if x < len(line_covariates):
                response += weight * line_covariates[x]

        return response + self.weights[-1]

    def diff(self, respone, covariate):
        return self._predict_one(covariate) - respone[0]

    """ for _ in range(iterations_number):  
            if _ % 1000 == 0:
                    print("Iteration:", _)
            for covariate, response in zip(train_covariates, train_response):
                for x, weight in enumerate(self.weights):
                    for x in range(len(self.weights)):
                        pred_response_and_real_response_diff = self.diff(response, covariate)
                        if  skip_side_values is False or pred_response_and_real_response_diff <= mistake_to_skip or _  < interations_b4_skip:
                            self.weights[x] -= learing_rate * pred_response_and_real_response_diff
                for x, weight in reversed(list(enumerate(self.weights))):
                    if double_learn:
                        for x in reversed(range(len(self.weights))):
                            pred_response_and_real_response_diff = self.diff(response, covariate)
                            if  skip_side_values is False or pred_response_and_real_response_diff <= mistake_to_skip or _  < interations_b4_skip:
                                self.weights[x] -= learing_rate * pred_response_and_real_response_diff
                if additional_rand_learn:
                    pred_response_and_real_response_diff = self.diff(response, covariate)
                    if  skip_side_values is False or pred_response_and_real_response_diff <= mistake_to_skip or _  < interations_b4_skip:
                        self.weights[x] -= learing_rate * pred_response_and_real_response_diff
                        rand = randint(0, len(self.weights)-1)
                        self.weights[rand] -= learing_rate * pred_response_and_real_response_diff"""