import csv
import re

lines_to_write = []
with open("data.txt", "r") as f:
    lines = f.readlines()
    count = 1
    for line in lines:
        line = line.strip()
        line = re.sub(' +', ';', line)
        if count % 2 == 0:
            lines_to_write[len(lines_to_write) - 1] = lines_to_write[len(lines_to_write) - 1] + ";" + line
        else:
            lines_to_write.append(line)
        count += 1

rows = []
for line in lines_to_write:
    rows.append(line.split(";"))

headers = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]

with open("boston-house.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)
