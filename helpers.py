import csv


def csv_parser(file, delimeter=' '):
    with open(file, 'r') as f:
        reader = csv.reader(f, delimeter)
        phones = []
        for row in reader:
            phones.append(row)
        return phones
