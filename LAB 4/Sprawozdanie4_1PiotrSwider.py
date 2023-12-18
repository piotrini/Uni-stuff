from random import randint

def create_random_array():
    array = []
    for _ in range(20):
        array.append(randint(10,50))

    return array

def selection_sort(array):
    for element in range(len(array)-1):
        min_value = array[element]
        min_pos = element
        for index in range(element+1, len(array)):
            if array[index] > min_value:
                min_value = array[index]
                min_pos = index
        _ = array[element]
        array[element] = array[min_pos]
        array[min_pos] = _
        print(array)

    return array

def find_max(array):
    max = 0
    for element in array:
        if element > max:
            max = element
    return max

def find_min(array):
    min = 51
    for element in array:
        if element < min:
            min = element
    return min

array = create_random_array()
# print(array)
print(selection_sort(array))
print("Wartość minimalna: "+str(find_min(array)))
print("wartość maksymalna: "+str(find_max(array)))
# print(bubble_sort(array))