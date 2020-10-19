import random
import math


def split_data(data, inputs, output, training_size, separator):       #split data to test and learn, data to wejsc, result to wyjscie
    headers = data.readline().split(separator)
    headers[-1] = headers[-1].replace('\n', "")
    
    temp_lines = data.readlines()
    lines = []
    
    for line in temp_lines:
        lines.append(line.replace('"', ""))

    #spliting data from string to list
    for i, line in enumerate(lines):
        lines[i] = line.split(separator)
        lines[i][-1] = lines[i][-1].replace("\n","")

    random.shuffle(lines)

    #finding indexes of needed headers
    wanted_headers_indexes_input = []
    for inp in inputs:
        try:
            wanted_headers_indexes_input.append(string_numer_to_int(headers.index(inp)))
        except ValueError:
             print(inp," is not valid value. Cannot find in headers")
             return
    try:
        wanted_header_indexes_output = string_numer_to_int(headers.index(output))
    except ValueError:
            print(output," is not valid value. Cannot find in headers")
            return

    #cutting data, to get only inputs and output
    cutted_lines_inputs = []
    cutted_lines_output = []
    for i, line in enumerate(lines):
        cutted_lines_inputs.append([])
        cutted_lines_output.append([])
        for y, variable in enumerate(line):
            if y in wanted_headers_indexes_input:
                cutted_lines_inputs[i].append(string_numer_to_int(variable))
            elif y is wanted_header_indexes_output:
                cutted_lines_output[i].append(string_numer_to_int(variable))

    """for x, line in enumerate(cutted_lines_inputs):
        print(cutted_lines_inputs[x])
        cutted_lines_inputs[x] = scale(line)"""
    
    training_data_inputs = []
    training_data_output = []

    testing_data_inputs = []
    testing_data_output = []

    training_size = int(training_size * len(lines)-1)

    for ind in range(training_size):
        training_data_inputs.append(cutted_lines_inputs[ind])
        training_data_output.append(cutted_lines_output[ind])

    for ind in range(len(lines) - training_size):
        testing_data_inputs.append(cutted_lines_inputs[training_size + ind])
        testing_data_output.append(cutted_lines_output[training_size + ind])

    return training_data_inputs, training_data_output, testing_data_inputs, testing_data_output

def scale(data):    #scales data to 0 - 1
    for i, d in enumerate(data):
        if type(d) == int or '9'>=d >= '0':
            data[i] = math.tanh(int(d))
    return data

def string_numer_to_int(number):
    if type(number) == str and '9'>=number >= '0':
        return int(number)
    return number
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