import csv


def package_comparison(package, return_package):
    return bool(package == return_package)


def clear_file(filename):
    f = open(filename, "w")
    f.close()


def save_results(filename, csvdata):
    f = open(filename, "a", newline="")
    writer = csv.writer(f, delimiter=";")
    for tup in csvdata:
        writer.writerow(tup)
    f.close()
