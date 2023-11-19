import csv

names = {}

with open("data.txt", "r") as f:
    for line in f.readlines():
        splitted = line.split("\"")
        id = splitted[0].strip()
        names[id] = splitted[1].strip()


header = ['Source', 'Target', 'Type', 'Id', "Label", "Timeset", "Weight"]

with open("edges.txt", "r") as f, open('output.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)
    id = 0
    for line in f.readlines():
        splitted = line.split(" ")
        first_name = names[splitted[0].strip()]
        second_name = names[splitted[1].strip()]
        writer.writerow([first_name, second_name, "Undirected", id])
        id += 1

