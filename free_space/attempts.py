import re

lines_to_write = []
with open("file_work_csv_txt/data.txt", "r") as f:
    lines = f.readlines()
    count = 1
    for line in lines:
        line = line.strip()
        line = re.sub(' +', ' ', line)
        if count % 2 == 0:
            lines_to_write[len(lines_to_write) - 1] = lines_to_write[len(lines_to_write) - 1] + " " + line + "\n"
        else:
            lines_to_write.append(line)
        count += 1

with open("file_work_csv_txt/new_data.txt", "w") as f:
    for line_write in lines_to_write:
        f.write(line_write)
