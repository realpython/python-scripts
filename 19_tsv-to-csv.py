import os
import sys
import csv


def convert(input, out):
    if os.path.exists(out):
        raise ValueError("Output file already exists")

    reader = csv.reader(open(input, 'rU'), dialect=csv.excel_tab)
    writer = csv.writer(open(out, "wb+"), dialect="excel")
    for row in reader:
        writer.writerow(row)

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])
