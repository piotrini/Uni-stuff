from random import randint

def create_random_array(array_length, min_element_value, max_element_value):
    array = []
    for _ in range(array_length):
        array.append(randint(min_element_value,max_element_value))
    
    return array

def find_array_leader(array):
    dominant = None
    max_count = 0
    dominant = array[0]
    if_leader_exist = None
    for compared_element in range(len(array)):
        element = array[compared_element]
        if dominant != element:
            count = 1
            for _ in range(compared_element+1, len(array)):
                if array[_] == element:
                    count += 1
            if count > max_count:
                max_count = count
                dominant = element
    if max_count > len(array)/2:
        if_leader_exist = True
    else:
        if_leader_exist = False
    return dominant, max_count, if_leader_exist


array = create_random_array(5,1,3)

print(array)
print(find_array_leader(array))
