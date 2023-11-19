import csv

headers = ["name"]
headers.extend([str(x) for x in range(1, 61)])

with open('sonar.mines', 'r') as f:
    startGrab = False
    trained = False
    train_set = {}
    test_set = {}
    name = ""
    column_name = 0
    row_lines = []
    for line in f.readlines():
        if "CM" in line:
            startGrab = True
            trained = False
            name = line
            name = name.replace("\n", "").replace(":", "").strip()
        elif startGrab:
            line = line.replace("\n", "")

            if line.isspace():
                if "*" in name:
                    name = name.replace("*", "")
                    train_set[name] = row_lines
                else:
                    test_set[name] = row_lines

                startGrab = False
                row_lines = []
            else:
                if "{" in line:
                    line = line[1:]
                elif "}" in line:
                    line = line[:-1]

                nums = list(filter(lambda x: x != "", line.split(" ")))
                row_lines.extend(nums)


with open("mines_train.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)

    for key, value in train_set.items():
        rows = [key]
        rows.extend(value)
        writer.writerow(rows)

with open("mines_test.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)

    for key, value in test_set.items():
        rows = [key]
        rows.extend(value)
        print(rows)
        writer.writerow(rows)
