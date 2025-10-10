import csv
import random

temperature = []
pressure    = []

for i in range(10):
    temp  = round(random.uniform(70, 85), 2)
    press = round(random.uniform(9.5, 11.5), 2) 
    temperature.append(temp)
    pressure.append(press)

with open('engine_log.csv', mode='w', newline='') as  file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['No', 'Temperatures', 'Pressures'])

    for i in range(len(temperature)):
        writer.writerow([i+1, temperature[i], pressure[i]])

print(f"Data simulasi berhasil disimpan pada engine_log.csv")