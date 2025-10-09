from colorama import Fore, Style
import random
import time

def get_sensor_data():
    # Simulasi data suhu dan tekanan kapal
    suhu = round(random.uniform(70, 90), 2)
    tekanan = round(random.uniform(9.5, 11.5), 2)
    return suhu, tekanan

def status_color(value, batas_normal, batas_berbahaya):
    if (value < batas_normal):
        return Fore.CYAN
    elif (value < batas_berbahaya):
        return Fore.YELLOW
    else:
        return Fore.RED

if __name__ == "__main__":
    print(Fore.GREEN + "=== Sistem Monitoring Mesin Kapal (Simulasi) ===" + Style.RESET_ALL)
    while True:
        suhu, tekanan = get_sensor_data()
        warna_suhu = status_color(suhu, 78, 85)
        warna_tekanan = status_color(tekanan, 10.5, 11.2)

        print(f"{warna_suhu}Suhu: {suhu}°C{Style.RESET_ALL} | {warna_tekanan}Tekanan: {tekanan} bar{Style.RESET_ALL}")
        time.sleep(1.6)