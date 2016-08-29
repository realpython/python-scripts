import csv
import sys
import json

"""
Example usage:

$ python 33_country_code.py 33_sample_csv.csv 33_country_codes.json
"""


def get_data(csv_file, json_file):
    countryCodes = []
    countryNames = []
    continentNames = []
    with open(csv_file, 'rt') as file_one:
        reader = csv.reader(file_one)
        with open(json_file) as file_two:
            json_data = json.load(file_two)
            all_countries = json_data["country"]
            for csv_row in reader:
                for json_row in all_countries:
                    if csv_row[0] == json_row["countryCode"]:
                        countryCodes.append(json_row["countryCode"])
                        countryNames.append(json_row["countryName"])
                        continentNames.append(json_row["continentName"])

    return [
        countryCodes,
        countryNames,
        continentNames
    ]


def write_data(array_of_arrays):
    with open('data.csv', 'wt') as csv_out:
        writer = csv.writer(csv_out)
        rows = zip(
            array_of_arrays[0],
            array_of_arrays[1],
            array_of_arrays[2]
        )
        for row in rows:
            writer.writerow(row)


if __name__ == '__main__':
    csv_file_name = sys.argv[1]
    json_file_name = sys.argv[2]
    data = get_data(csv_file_name, json_file_name)
    write_data(data)
