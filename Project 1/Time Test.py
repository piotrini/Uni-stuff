from random import randint
import time

def create_random_array(array_length,min_array_value = 0,max_array_value = 100):
    array = []
    for _ in range(array_length):
        array.append(randint(min_array_value,max_array_value))
    return array



def create_random_matrix(array_length,min_array_value = 0,max_array_value = 100):
    array = []
    matrix = []
    for _ in range(array_length):
        array = create_random_array(array_length)
        matrix.append(array)
    return matrix

start_time = time.time()
matrix = create_random_matrix(10,10)
print(matrix)
print("--- %s seconds ---" % (time.time() - start_time))