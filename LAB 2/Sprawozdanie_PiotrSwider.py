def create_array():
    array = []
    array_length = input("Wprowadz rozmiar tablicy: ")
    for x in range(int(array_length)):
        array_elements = int(input("Wprowadz element o indeksie "+str(x)+": "))
        array.append(array_elements)

    return array

def highlight_key_in_array(searched_key,array):
    for index in range(len(array)):
        if array[index] == searched_key:
            array[index] = str(searched_key)+"*"
        else: array[index] = str(array[index])

    return array

def logic_array(searched_key, array):
    array_length = len(array)
    return_array = [False for i in range(array_length)]
    for index in range(array_length):
        if array[index] == searched_key:
            return_array[index] = True

    return return_array

def key_count(searched_key, array):
    key_count = 0
    for element in array:
        if element == searched_key:
            key_count += 1
    return key_count

def pos_of_key_in_first_half(searched_key, array_length, array):
    first_pos_of_key = -1
    for index in range(array_length // 2):
        if array[index] == searched_key:
            first_pos_of_key = index + 1
            break
    return first_pos_of_key

def pos_of_key_in_second_half(searched_key, array_length, array):
    first_pos_of_key = -1
    for index in range(array_length//2, array_length):
        if array[index] == searched_key:
            first_pos_of_key = index + 1
            break
    return first_pos_of_key

array = create_array()
searched_key = int(input("Wprowadz klucz: "))
print(pos_of_key_in_second_half(searched_key, len(array),array))
print(array)
# print("Pierwsza pozycja klucza w pierwszej polowie tablicy: ", end="")
# print(pos_of_key_in_first_half(searched_key,len(array),array))
# print(key_count(searched_key,array))
# star_array = highlight_key_in_array(searched_key, array)
# print(star_array)
# print(logic_array(searched_key,array))
