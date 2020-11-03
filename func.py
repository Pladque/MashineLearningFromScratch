import random
import math

def split_data(data, covariate_headers, response_header, training_size, separator, shuffle = True, unwanted_sings = [], new_line_sing = '\n'):       #split data to test and learn, data to wejsc, result to wyjscie
    headers = data.readline().split(separator)
    headers[-1] = headers[-1].replace(new_line_sing, "")
    
    temp_lines = data.readlines()
    lines = []
    
    for line in temp_lines:
        for sign in unwanted_sings:
            lines.append(line.replace(sign, ""))

    #spliting data from string to list
    for i, line in enumerate(lines):
        lines[i] = line.split(separator)
        lines[i][-1] = lines[i][-1].replace("\n","")

    if shuffle:
        random.shuffle(lines)

    #finding indexes of needed headers
    wanted_headers_indexes_input = []
    for inp in covariate_headers:
        try:
            wanted_headers_indexes_input.append(string_numer_to_float(headers.index(inp)))
        except ValueError:
             print(inp," is not valid value. Cannot find in headers")
             return
    try:
        wanted_header_indexes_output = string_numer_to_float(headers.index(response_header))
    except ValueError:
            print(response_header," is not valid value. Cannot find in headers")
            return

    #cutting data, to get only covariates and response
    cutted_lines_covariates = []
    cutted_lines_response = []
    for i, line in enumerate(lines):
        cutted_lines_covariates.append([])
        cutted_lines_response.append([])
        for y, variable in enumerate(line):
            if y in wanted_headers_indexes_input:
                cutted_lines_covariates[i].append(string_numer_to_float(variable))
            elif y is wanted_header_indexes_output:
                cutted_lines_response[i].append(string_numer_to_float(variable))
    
    training_data_covariates = []
    training_data_response = []
    testing_data_covariates = []
    testing_data_response = []

    training_size = int(training_size * len(lines)-1)

    for ind in range(training_size):
        training_data_covariates.append(cutted_lines_covariates[ind])
        training_data_response.append(cutted_lines_response[ind])

    for ind in range(len(lines) - training_size):
        testing_data_covariates.append(cutted_lines_covariates[training_size + ind])
        testing_data_response.append(cutted_lines_response[training_size + ind])

    return training_data_covariates, training_data_response, testing_data_covariates, testing_data_response, 

def string_numer_to_float(element):
    if type(element) == str and element.replace('.','',1).isdigit():
        return float(element)
    return element

def save_model(model, file_name = "weights.cfg"):
    with open(file_name, "w") as f:
        for weight in model.weights:
            f.write(str(weight))
            f.write(" ; ")
    print("model saved succesfully")

def load_model(model, file_name = "weights.cfg"):
    try:
        with open(file_name, "r") as f:
            weights = f.readline()
        weights = weights.split(';')
        weights.pop(-1) #bc last is empty string
        if is_weights_valid(weights) is False:     #means if file is empty
            print("model loaded failure. Check if file is not empty and if it contains valid weights")
            return False

        weights = [float(weight) for weight in weights]
        
        model = model.load_weights(weights)
        print("model loaded succesfully")
    except:
        return False
    return True

def scale(data, custom_divider = False, index = False):
    if custom_divider is not False and index is False:
        for x in range(len(data[0])):
            for y, line in enumerate(data):
                data[y][x] = line[x]/custom_divider
    elif custom_divider is not False and index is not False:
        data = [line[index]/custom_divider for line in data]

    else:
        for x in range(len(data[0])):
            max = float("-inf")
            for y, line in enumerate(data):
                if max < line[x]:   max = line[x]
            for y, line in enumerate(data):
                data[y][x] = line[x]/max
    return data


def get_index_of_header(headers, name):
    return headers.index(name)

def non_int_covariates_to_int(lines, header, headers, ordered_data):
    index = get_index_of_header(headers, header)
    for x,line in enumerate(lines):
        data_value_string = line[index]
        lines[x][index] = int(line[index].replace(data_value_string, str(ordered_data.index(data_value_string))))

    return lines

def is_weights_valid(weights):
    for weight in weights:
        try:
            float(weight)
        except:
            return False
    return True
