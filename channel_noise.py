import random


def binary_symmetric_channel(package, p):
    return_package = ""
    for element in package:
        x = random.uniform(0, 1)
        if x < p:
            if element == '1':
                return_package = return_package + '0'
            else:
                return_package = return_package + '1'
        else:
            return_package = return_package + element
    return return_package
