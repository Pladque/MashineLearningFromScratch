class Model:

    def __init__(self,inputs_number, start_weight_value, ):
        self.weights = []   #chyba bd potrzebowal inputs_number+1 zeby miec wykres dobry(w[0]+w[1]*x[0]+w[2]*x[1] itd..)
        for _ in range(inputs_number):
            self.weights.append(start_weight_value)
        self.weights.append(start_weight_value)

    def train(self, train_covariates, train_response): # amount_of_learns):        
        
        average_cowariates = []
        average_response = 0

        for _ in range(len(train_covariates[0])):
            average_cowariates.append(0)
        
        for i, covariates in enumerate(train_covariates):
            for x, covariate in enumerate(covariates):
                average_cowariates[x] += covariate
        
        print(average_cowariates)

        for _train_response in train_response:
            average_response += _train_response[0]

        for x, covariate in enumerate(average_cowariates):
            average_cowariates[x] = covariate / len(train_covariates)

        average_response = average_response / len(train_response) 

        print(average_response)
        print(average_cowariates[0])
        print(average_cowariates[1])
        #everithing above is good
        #everithing below is pure garbage
        ingredient = []

        for i, covariates in enumerate(train_covariates):
            ingredient.append([])
            for x, covariate in enumerate(covariates):
                ingredient[i].append(covariate - average_cowariates[x])
            ingredient[i].append(train_response[i][0] -  average_response)   


    def test(self,test_covariates, test_response, if_print = False):
        average_mistake = 0
        for test_input, test_output in zip(test_covariates,test_response):
            if if_print:
                print("PREDICTED: ",self.predict(test_input)," ACTUAL: ", test_output, 
                "COVARIATES: ",test_input,
                "MISTAKE: ", abs(self.predict(test_input)[0]-test_output[0]),'points; ', 
                )
            average_mistake += abs(self.predict(test_input)[0]-test_output[0])
        return average_mistake/ len(test_response)
         
    def predict(self, covariates): #returns what number model will predict
        response = 0
        for x, weight in enumerate(self.weights):
            if x < len(covariates):
                response += weight * covariates[x]
        response += self.weights[-1]        #last element in list a constant term
        return [response]