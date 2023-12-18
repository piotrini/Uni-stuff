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
# print(matrix)
def get_submatrix(matrix, x, y, width, height):
    return [row[x:x+width] for row in matrix[y:y+height]]

def get_matrix_sum(matrix):
    sum = 0
    for row in matrix:
        for element in row:
            sum += element
    return sum

def find_submatrices_summing_above_threshhold(matrix, threshhold, submatrix_width = 2, submatrix_height = 2):
    results = []
    for y in range((len(matrix)-submatrix_height+1)):
        for x in range((len(matrix[0])-submatrix_width+1)):
            submatrix = get_submatrix(array, x, y, submatrix_width, submatrix_height)
            if(get_matrix_sum(submatrix) >= threshhold):
                results.append(submatrix)
    return results
import time
start_time = time.time()
k = 25
array_length = 2000
# array = [[9,2,3,4,5],[9,7,1,8,6],[1,9,9,0,11]]  
array = create_random_matrix(array_length)
print(find_submatrices_summing_above_threshhold(array, k))
find_submatrices_summing_above_threshhold(array, k)
print("Dla wielkosci: "+str(array_length))
print("--- %s seconds ---" % (time.time() - start_time))


