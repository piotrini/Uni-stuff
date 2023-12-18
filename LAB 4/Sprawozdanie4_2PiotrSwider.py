from random import randint

def create_array():
    array = []
    for _ in range(20):
        array.append(randint(0,99))

    return array

def bubble_sort(array):
    swapped = None
    for _ in range(len(array)-1):
        for x in range(0,len(array)-_-1):
            if array[x] < array[x+1]:
                swapped = True
                array[x], array[x+1] = array[x+1], array[x]
            if swapped == False:
                continue
        print(array)
    return array


array = create_array()

print(bubble_sort(array))

