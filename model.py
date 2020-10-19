class Model:

    def __init__(self,inputs_number, start_weight_value, ):
        self.weights = []   #chyba bd potrzebowal inputs_number+1 zeby miec wykres dobry(w[0]+w[1]*x[0]+w[2]*x[1] itd..)
        for _ in range(inputs_number):
            self.weights.append(start_weight_value)

    def train(self, input_data, output_data, amount_of_learns):        
        pass

    def test(self,test_input_data, test_output_data):
        pass
         

    def _predict(self, inputs): #here it will
        pass