import csv

with open('engine_log.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        no, temp, press = row
        print(f"Data no-{no} : Suhu = {temp}°C : Tekanan = {press} bar")