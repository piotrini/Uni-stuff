from random import randint

def create_array():
    array = []
    for x in range(10):
        array.append(randint(-10,10))
    return array

def get_max_element(array):
    max = -10
    for x in array:
        if x > max:
            max = x
    return max

def get_min_element(array):
    min = 10
    for x in array:
        if x < min:
            min = x
    return min

def get_min_nat_element(array):
    min_nat = 10
    for x in array:
        if 0 < x < min_nat:
            min_nat = x
    return min_nat

def get_min_nat_even_element(array):
    min_nat_even = 10
    for x in array:
        if x%2==0 and x > 0:
            min_nat_even = x
    return min_nat_even

def get_first_odd_element(array):
    odd_element = 0
    for x in array:
        if x%2!=0:
            odd_element = x
            break
    return odd_element

def get_second_odd_element(array):
    element_sum = []
    for x in array:
        if x%2!=0:
            element_sum.append(x)
            if len(element_sum) > 1:
                return element_sum[1]
    return -11       
            




array = create_array()
print("Tablica: ", end="")
print(array)
print("a) Najwiekszy element tablicy: ", end="")
print(get_max_element(array))
print("b) Najmniejszy element tablicy: ", end="")
print(get_min_element(array))
print("c) Najmniejsza wartosc dodatnia: ", end="")
print(get_min_nat_element(array))
print("d) Najmniejsza wartosc dodatnia, parzysta: ", end="")
print(get_min_nat_even_element(array))
print("e) Pierwsza nieparzysta liczba tablicy: ", end="")
print(get_first_odd_element(array))
print("f) Druga nieparzysta liczba tablicy: ", end="")
print(get_second_odd_element(array))