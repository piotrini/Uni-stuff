from random import randint

def create_array():
    array = []
    for x in range(100):
        array.append(randint(0,9))
    return array

def search_key_in_array_static(searched_key, array):
    array_length = len(array)
    return_array = [False for i in range(array_length)]
    for index in range(array_length):
        if array[index] == searched_key:
            return_array[index] = True
    return return_array

def search_key_in_array_dynamic(searched_key, array):
    return_array = []
    for index in range(len(array)):
        if array[index] == searched_key:
            return_array.append(index)
    return return_array

array = create_array()
random_number = randint(0,9)
print("Tablica: ")
print(array, end="\n\n")

print("a) Wszystkie wystapienia klucza z uzyciem drugiej tablicy: ")
print(search_key_in_array_static(random_number, array), end="\n\n")

print("b) Wszystkie wystapienia klucza z uzyciem tablicy o dynamicznej dlugosci: ")
print(search_key_in_array_dynamic(random_number, array), end="\n\n")
