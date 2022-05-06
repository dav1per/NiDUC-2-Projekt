import random


def packages(number_of_packages, package_length):
    packages = []

    for x in range(0, number_of_packages):
        message = ''
        for y in range(0, package_length):
            bit = random.randint(0, 1)
            message = message + str(bit)
        packages.append(message)
    return packages


def packages_pb(number_of_packages, package_length):
    packages = []

    for x in range(0, number_of_packages):
        message = ''
        bit1 = 0
        for y in range(0, package_length):
            bit = random.randint(0, 1)
            message = message + str(bit)
            if bit == 1:
                bit1 += 1
        #even parity
        if bit1 % 2 == 0:
            message = message + '0'
        else:
            message = message + '1'
        packages.append(message)
    return packages
