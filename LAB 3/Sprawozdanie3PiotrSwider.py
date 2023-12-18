from random import randint

def create_random_array(array_length, min_element_value, max_element_value):
    array = []
    for _ in range(array_length):
        array.append(randint(min_element_value,max_element_value))
    return array

def find_dominant(array):
    max_count = 0
    operation_counter = 0
    dominant = None
    for compared_element in array:
        count = 0
        for element in array:
            if compared_element == array[element]:
                count +=1
                operation_counter +=1
        if count > max_count:
            max_count = count
            dominant = compared_element
    return max_count, dominant, operation_counter

def mark_dominant_and_anti_dominant_in_array(array, dominant, anti_dominant):
    for index in range(len(array)):
        if array[index] == dominant:
            array[index] = ">"+str(dominant)
        if array[index] == anti_dominant:
            array[index] = str(anti_dominant)+"*"
    return array

def first_and_last_pos_of_dominant(array):
    first_pos = None
    last_pos = None
    for index in range(len(array)-1):
        if array[index] == dominant:
            first_pos = index + 1
            break
    for index in range(len(array)-1,-1,-1):
        if array[index] == dominant:
            last_pos = index + 1
            break
    return first_pos, last_pos

def find_anti_dominant(array):
    min_count = len(array)
    operation_counter = 0
    anti_dominant = None
    for compared_element in array:
        count = 0
        for element in array:
            if compared_element == element:
                count +=1
                operation_counter +=1
        if count < min_count:
            min_count = count
            anti_dominant = compared_element
    return min_count, anti_dominant, operation_counter

array = create_random_array(200, 0, 99)
result = find_dominant(array)
dominant = result[1]
result_2 = find_anti_dominant(array)
anti_dominant = result_2[1]
# print(array)
# print(result)
# print(first_and_last_pos_of_dominant(array))
print(find_anti_dominant(array))
print(mark_dominant_and_anti_dominant_in_array(array, dominant, anti_dominant))
# print(result)
