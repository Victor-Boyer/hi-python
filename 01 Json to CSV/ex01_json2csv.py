import json
import csv

def getList(dict):
    return dict.keys()

nameJson = input("Please put the file in this folder and write the name : ")

fileJson = open("json.json", "r")
jsonArray = json.loads(fileJson.read())


if len(jsonArray) > 1:
    keys = getList(jsonArray[0])

    with open('csv.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(keys)
        values = []

        for line in jsonArray:
            for key in keys:
                if line[key]:
                    values.append(line[key])
                else:
                    values.append(" ")
            writer.writerow(values)
else:
    keys = getList(jsonArray[0])

    with open('csv.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(keys)
        values = []

        for key in keys:
            if jsonArray[0][key]:
                values.append(jsonArray[0][key])
            else:
                values.append(" ")
        writer.writerow(values)

