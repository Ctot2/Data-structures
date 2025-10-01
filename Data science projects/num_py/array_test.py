import numpy as np

array = np.array([5, 2, -5, 10, 23, -21])


def max_int_in_array(array):
    highest_value = array[0]
    if len(array) == 1:
        return array[0]
    else:
        for i in array:
            if highest_value < i:
                highest_value = i

    return highest_value



print(max_int_in_array(array))