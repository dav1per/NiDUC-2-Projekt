import generator
import channel_noise
import crc
import stats
import numpy as np

csvdata = []
filename = "ARQ_results_crc.csv"
package_length = 8
number_of_packages = 10000
n = 8
divisor = "111010101"

stats.clear_file(filename)

for p in np.arange(0.3, 0, -0.01):
    packages = generator.packages(number_of_packages, package_length)

    # stats
    arq_requests = 0
    correct_return_packages = 0

    for package in packages:
        package = crc.package(package, n)
        code = crc.crc(package, n, divisor, package_length)[package_length:package_length + n]
        package = package[:package_length] + code
        return_package = channel_noise.binary_symmetric_channel(package, p)
        while not crc.check(return_package, n, divisor, package_length):
            return_package = channel_noise.binary_symmetric_channel(package, p)
            arq_requests += 1
        if stats.package_comparison(package, return_package):
            correct_return_packages += 1
    percentage = correct_return_packages / number_of_packages * 100
    tup = (round(p, 2), arq_requests, correct_return_packages, round(percentage, 2))
    csvdata.append(tup)

stats.save_results(filename, csvdata)
