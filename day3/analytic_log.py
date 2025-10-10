import csv

temps = []
presses = []

with open('engine_log.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        temp = float(row['Temperatures'])
        press = float(row['Pressures'])
        temps.append(temp)
        presses.append(press)

avg_temp = sum(temps) / len(temps)
avg_press = sum(presses) / len(presses)

print(f"\nRata-rata suhu = {avg_temp:.2f}°C")
print(f"\nRata-rata tekanan = {avg_press:.2f} bar")

for t in temps:
    if t > 78:
        print(f"Suhu tinggi terdeteksi: {t:.2f}°C")

for p in presses:
    if p > 10.8:
        print(f"Tekanan tinggi terdeteksi: {p:.2f} bar")