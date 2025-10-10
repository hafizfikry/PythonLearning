import matplotlib.pyplot as plt
import pandas as pd
import time

df = pd.read_csv('engine_log.csv', delimiter=',')

temperatures = df['Temperatures']

# print(temperatures)

for index, row in df.iterrows():
    print(index)
    plt.plot(df['No'], df['Temperatures'], label='Temperature (°C)')
    plt.plot(df['No'], df['Pressures'], label='Pressure (bar)')

    plt.legend()
    plt.title("Engine Monitoring - Kapal Laut")
    plt.xlabel("Data Ke-")
    plt.ylabel("Nilai Sensor")
    plt.show()
    time.sleep(1.2)


# plt.plot(temperatures, label='Temperature (°C)')
# plt.plot(pressures, label='Pressure (bar)')