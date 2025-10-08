# Simulasi data sensor kapal
temperatures = [72.5, 73.0, 74.2, 75.1, 77.8, 80.3]
pressures = [10.2, 10.4, 10.1, 10.6, 10.8, 11.0]

print(f"Data suhu mesin kapal (°C) : {temperatures}")
print(f"Data tekanan mesin kapal (bar) : {pressures}")

print(sum(temperatures), len(temperatures))
print(sum(pressures), len(pressures))

avg_temp = sum(temperatures) / len(temperatures)
avg_press = sum(pressures) / len(pressures)

print(f"\nRata-rata suhu mesin kapal : {avg_temp:.2f}°C")
print(f"Rata-rata tekanan mesin kapal : {avg_press:.2f} bar")

for temp in temperatures:
    if(temp > 78):
        print(f"!!Suhu mesin kapal {temp}°C, melebihi batas aman!")

for press in pressures:
    if(press > 10.5):
        print(f"!!Tekanan mesin kapal {press} bar, tekanan terlalu besar!")