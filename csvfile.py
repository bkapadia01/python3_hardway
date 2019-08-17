import csv

with open('verification.csv') as csv_file:
    csv_read = csv.csv_read(csv_file, delimiter=',')
    line_count = 0
    for row in csv_read:
        while line_count == 0:
            print(f'{",".join(row)}')
        line_count += 1