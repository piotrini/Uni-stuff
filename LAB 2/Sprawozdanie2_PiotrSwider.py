from random import randint
def create_array():
    array = []
    array_length = 20
    for element in range(array_length):
        array.append(randint(-100,100))
    return array

def find_max(array):
    max = 0
    for element in array:
        if element > max:
            max = element
    return max

def how_many_max(array):
    how_many_max = 0
    for element in array:
        if element == max:
            how_many_max +=1
    return how_many_max

def find_max_pos(array):
    array_length = 20
    for index in range(array_length):
        if array[index] == max:
            find_max_pos = index+1
    return find_max_pos

def find_min_dod(array):
    min = 1000
    for element in array:
        if element < min and element > 0:
            min = element
    return min

def find_min(array):
    min = 1000
    for element in array:
        if element < min:
            min = element
    return min

array = create_array()
max = find_max(array)
print("Tablica:",end="")
print(array)
print("Ilosc wystapienia klucza (min): ", end="")
print(find_min(array))
# print("Ilosc wystapienia klucza (min_dod): ", end="")
# print(find_min_dod(array))
# print("Ilosc wystapienia klucza (max): ", end="")
# print(how_many_max(array))
# print("Wartość maksymalna tablicy: ", end="")
# print(find_max(array))
# print("Pozycja klucza (max): ", end="")
# print(find_max_pos(array))
