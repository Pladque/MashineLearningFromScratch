import random
import math


def split_data(data, covariate_headers, response_header, training_size, separator, shuffle = True):       #split data to test and learn, data to wejsc, result to wyjscie
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

    if shuffle:
        random.shuffle(lines)

    #finding indexes of needed headers
    wanted_headers_indexes_input = []
    for inp in covariate_headers:
        try:
            wanted_headers_indexes_input.append(string_numer_to_int(headers.index(inp)))
        except ValueError:
             print(inp," is not valid value. Cannot find in headers")
             return
    try:
        wanted_header_indexes_output = string_numer_to_int(headers.index(response_header))
    except ValueError:
            print(response_header," is not valid value. Cannot find in headers")
            return

    #cutting data, to get only covariates and outpuresponse
    cutted_lines_covariates = []
    cutted_lines_response = []
    for i, line in enumerate(lines):
        cutted_lines_covariates.append([])
        cutted_lines_response.append([])
        for y, variable in enumerate(line):
            if y in wanted_headers_indexes_input:
                cutted_lines_covariates[i].append(string_numer_to_int(variable))
            elif y is wanted_header_indexes_output:
                cutted_lines_response[i].append(string_numer_to_int(variable))

    """for x, line in enumerate(cutted_lines_covariates):
        print(cutted_lines_covariates[x])
        cutted_lines_covariates[x] = scale(line)"""
    
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

def scale(data):    #scales data to 0 - 1
    for i, d in enumerate(data):
        if type(d) == int or '9'>=d >= '0':
            data[i] = math.tanh(int(d))
    return data

def string_numer_to_int(number):    #it has no sens, fix later
    if type(number) == str and '9'>=number >= '0':
        return int(number)
    return number

def find_index_of_header_list(covariate_headers):
    pass

def get_index_of_header(headers, name):
    return headers.index(name)

def non_int_covariates_to_int(lines, header, headers, ordered_data):
    index = get_index_of_header(headers, header)
    for x,line in enumerate(lines):
        data_value_string = line[index]
        lines[x][index] = int(line[index].replace(data_value_string, str(ordered_data.index(data_value_string))))  #convert it to int leter


    return lines