import csv

# with open("todos.csv") as f:
#     for line in f:
#         print(line.strip())

# print("-" * 50)

# with open("todos.csv") as f:
#     reader = csv.reader(f)

#     for line in reader:
#         print(line)

data = [
    ["id", "name", "is_retired"],
    ["1", "John", "false"],
    ["2", "Adam", "true"],
]

with open("todos1.csv", "wt", newline='') as f:
    writer = csv.writer(f)
    for line in data:
        writer.writerow(line)
