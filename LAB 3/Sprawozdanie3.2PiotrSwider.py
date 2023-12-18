from random import randint

def create_random_array(array_length, min_element_value, max_element_value):
    array = []
    for _ in range(array_length):
        array.append(randint(min_element_value,max_element_value))
    return array

array = create_random_array(200,0,99)

print(array)

def find_min_and_max(array):
    if array[0] > array[1]:
        min = array[1]
        max = array[0]
    else:
        min = array[0]
        max = array[1]

    for index in range(2, len(array),2):
        if array[index] > array[index + 1]:
            if array[index] > max:
                max = array[index]
            if array[index+1] < min:
                min = array[index+1]
        else:
            if array[index] < min:
                min = array[index]
            if array[index+1] > max:
                max = array[index+1]

    return min, max

print(find_min_and_max(array))