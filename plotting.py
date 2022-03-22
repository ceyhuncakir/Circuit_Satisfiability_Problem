import csv

def plot():
    with open('spreadsheet/data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        print(csv_reader)

plot()
