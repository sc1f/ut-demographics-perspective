import os
import csv
import string
import re

def string_to_int(in_str):
    if re.findall(r"\d", in_str):
        in_str.translate(str.maketrans('', '', string.punctuation)) # remove punctuation
        return int(in_str)
    return in_str

def parse(csv):
    data = []
    for row in csv:
        del row[-2]
        for i in range(1, len(row)):
            if row[i] == '':
                row[i] = 0
                continue
            row[i] = string_to_int(row[i])
        data.append(row)
    return data

if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, "../csv/ut_demographics.csv")) as in_csv:
        reader = csv.reader(in_csv)
        data = parse(reader)
        with open(os.path.join(dirname, "../static/csv/demographics.csv"), "w+") as out_csv:
            writer = csv.writer(out_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in data:
                writer.writerow(row)



