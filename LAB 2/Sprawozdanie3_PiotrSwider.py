from random import randint

def create_array():
    array = []
    array_length = 15
    for element in range(array_length):
        array.append(randint(1,1000))
    return array

def find_max(array):
    max = 0
    for element in array:
        if element > max:
            max = element
    return max

def find_min(array):
    min = 1000
    for element in array:
        if element < min:
            min = element
    return min

def find_max_and_min_pos(array):
    array_length = 15
    for index in range(array_length):
        if array[index] == max:
            max_pos = index+1
        if array[index] == min:
            min_pos = index+1
    return max_pos, min_pos
    
def how_many_max_and_min(array):
    how_many_max = 0
    how_many_min = 0
    for element in array:
        if element == max:
            how_many_max += 1
        if element == min:
            how_many_min +=1
    return how_many_min, how_many_max

def how_many_max(array):
    how_many_max = 0
    for element in array:
        if element == max:
            how_many_max += 1
    return how_many_max

def how_many_min(array):
    how_many_min = 0
    for element in array:
        if element == min:
            how_many_min += 1
    return how_many_min

def which_value_more_often(array):
    if how_many_max > how_many_min:
        return print("Czesciej wystepuje wartosc maksymalna w tej tablicy", end="")
    if how_many_min > how_many_max:
        return print("Czesciej wystepuje wartosc minimalna w tej tablicy", end="")
    else: 
        return print("Wartosc maksymalna i minimalna wystepuja w takiej samej czestotliwosci")

def which_value_first(array):
    if min_pos > max_pos:
        return print("Wartosc minimalna jest pierwsza")
    else: return print("Wartosc maksymalna jest pierwsza")

def min_and_max_pos_subtract(array):
    if max_pos > min_pos:
        return max_pos - min_pos
    else: return min_pos - max_pos

def reversed_find_max_and_min(array):
    for index in range(len(array)-1,0,-1):
        if array[index] == max:
            max_pos_reversed = index+1
        if array[index] == min:
            min_pos_reversed = index+1
    return max_pos_reversed, min_pos_reversed
    
array = create_array()
min = find_min(array)
max = find_max(array)
how_many_max = how_many_max(array)
how_many_min = how_many_min(array)
max_pos = find_max_and_min_pos(array)[0]
min_pos = find_max_and_min_pos(array)[1]
max_pos_reversed = reversed_find_max_and_min(array)
min_pos_reversed = reversed_find_max_and_min(array)

print("Tablica:", end="")
print(array)
print("Pozycje kolejno wartości maksymalnej i minimalnej tablicy: ", end="")
print(find_max_and_min_pos(array))
print("Ilosc wystapien kolejno wartosci minimalnej i maksymalnej: ", end="")
print(how_many_max_and_min(array))
# print(which_value_more_often(array))
# print(which_value_first(array))
print("Odleglosc wartosci minimalnej i maksymalnej to: ", end="")
print(min_and_max_pos_subtract(array))