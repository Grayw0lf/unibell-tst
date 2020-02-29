import csv


def csv_parser(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        phones = []
        for row in reader:
            phones.append(row)
        return phones
