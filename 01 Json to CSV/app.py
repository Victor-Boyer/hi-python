import json
import csv
import sys

def convertor(file) :
    print(file)
    input_file = open(file, "r")
    output_file = open(file + ".csv", "w")
    writer = csv.writer(output_file)

    for row in json.loads(input_file.read()) :
        writer.writerow(row)


convertor(sys.argv[1])