from random import randint

def create_random_array(array_length, min_element_value, max_element_value):
    array = []
    for _ in range(array_length):
        array.append(randint(min_element_value,max_element_value))
    return array

def mark_dominant_in_array(array, dominant):
    for index in range(len(array)):
        if array[index] == dominant:
            array[index] = ">"+str(dominant)
    return array

def find_dominant_in_array(array):
    max_count = 0
    operation_counter = 0
    dominant = array[0] - 1;
    for compared_element in range(len(array)-max_count):
        element = array[compared_element]
        if dominant != element:
            count = 1
            for _ in range(compared_element+1,len(array)):
                if array[_] == element:
                    count += 1
                    operation_counter += 1
            if count > max_count:
                max_count = count
                dominant = element
    return dominant, max_count, operation_counter

def check_if_dominant_closer_to_min_or_max(array, dominant):
    max = 0
    min = 99
    for element in array:
        if element > max:
            max = element
        if element < min:
            min = element
    if abs(dominant - max) > abs(dominant - min):
        return "Dominanta jest blizej wartosci max"
    else: return "Dominanta jest blizej waratosci min"

array = create_random_array(200,0,99)
result_1 = find_dominant_in_array(array)
dominant = result_1[0]
# print(mark_dominant_in_array(array,1))

print(find_dominant_in_array(array))

print(check_if_dominant_closer_to_min_or_max(array,dominant))