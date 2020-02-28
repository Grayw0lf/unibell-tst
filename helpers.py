import csv
import json


def csv_to_json(file):
    json_data = [json.dumps(f) for f in csv.DictReader(open(file))]
    return json_data
