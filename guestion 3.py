import random, time
import matplotlib.pyplot as plt

temps = []
humidities = []

for t in range(10):
    temp = 25 + random.uniform(-1, 1)
    humidity = 60 + random.uniform(-5, 5)
    temps.append(temp)
    humidities.append(humidity)
    time.sleep(0.5)

    try:
        with open("temps_humidity.csv", "a") as csv_f:
            csv_f.write(f"{t},{temp},{humidity}\n")
            with open("temps_humidity.txt", "a") as txt_f:
                txt_f.write(f"Time: {t}s, Temperature: {temp:.2f}C, Humidity: {humidity:.2f}%\n")
    except IOError as e:
        print(f"Error writing to file: {e}")
        plt.figure(figsize=(10, 6))
plt.plot(temps, label='Temperature (C)')
plt.plot(humidities, label='Humidity (%)')
plt.xlabel("Time (s)")
plt.ylabel("Value") 
plt.title("Temperature and Humidity Over Time")
plt.legend()
plt.grid(True)
plt.show()
