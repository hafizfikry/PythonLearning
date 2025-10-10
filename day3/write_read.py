import csv

with open('data.txt', 'w') as file:
    file.write("Ini data suhu mesin kapal.\n")
    file.write("Suhu rata-rata: 75.3°C\n")

with open('data.txt', 'r') as file:
    content = file.read()
    print(content)