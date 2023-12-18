from random import randint

def create_random_array(array_length, min_element_value, max_element_value):
    array = []
    for _ in range(array_length):
        array.append(randint(min_element_value,max_element_value))
    return array

def sort_array(array):
    for element in range(len(array)-1):
        min = array[element]
        min_pos = element
        index = element + 1
        for index in range(index<len(array)):
            if array[index] < min:
                min = array[index]
                min_pos = index
        x = array[element]
        array[element] = array[min_pos]
        array[min_pos] = x
    return array

array = create_random_array(200,0,99)
print(sort_array(array))