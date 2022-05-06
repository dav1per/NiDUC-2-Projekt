import generator
import channel_noise
import stats
import numpy as np


csvdata = []
filename = "without_ARQ_results_pb.csv"
package_length = 8
number_of_packages = 10000

stats.clear_file(filename)

for p in np.arange(0.8, 0, -0.01):
    packages = generator.packages_pb(number_of_packages, package_length)

    # stats
    incorrect_return_packages = 0
    correct_return_packages = 0

    for package in packages:
        return_package = channel_noise.binary_symmetric_channel(package, p)
        if stats.package_comparison(package, return_package):
            correct_return_packages += 1
        else:
            incorrect_return_packages += 1
    percentage_correct = correct_return_packages / number_of_packages * 100
    percentage_incorrect = incorrect_return_packages / number_of_packages * 100
    tup = (round(p, 2), correct_return_packages, round(percentage_correct, 2), incorrect_return_packages, round(percentage_incorrect, 2))
    csvdata.append(tup)

stats.save_results(filename, csvdata)
