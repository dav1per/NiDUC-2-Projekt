def check(return_package, package_length):
    bit1 = 0
    for i in range(0, package_length):
        if return_package[i] == '1':
            bit1 += 1
    if bit1 % 2 == 0:
        parity_bit = '0'
    else:
        parity_bit = '1'
    return bool(return_package[package_length] == parity_bit)





