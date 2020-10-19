
def split_data(data, input, output, training_size, separator):       #split data to test and learn, data to wejsc, result to wyjscie
    headers = (data.readline().split(separator))

    temp_lines = data.readlines()
    lines = []
 
    for line in temp_lines:
        lines.append(line.replace('"', ""))

    for i, line in enumerate(lines):
        lines[i] = line.split(separator)
        lines[i][-1] = lines[i][-1].replace("\n","")

    print(lines[0])

def shuffle_data(data):
    pass


def scale(data):    #scale data to 0 - 1
    pass

def model_fitness(data, results, model):     #returns how close model were
    pass

def train(model, input_data, output_data):        
    pass

def adjust_weights(model):
    pass

def round_results(result, precision):  #precison: how many digits after coma. Adjust that value by analising data
    pass

def calculate_error_rate():
    pass