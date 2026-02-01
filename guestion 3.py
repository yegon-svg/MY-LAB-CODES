import random, time
import matplotlib.pyplot as plt

temps = []
humidity_data = [] 

for t in range(10):
    temp = 25 + random.uniform(-1, 1)
    humidity = random.uniform(40, 60)
    temps.append(temp)
    humidity_data.append(humidity) 
    
time.sleep(0.5)

try:
    with open("temps.csv", "w") as f:
        f.write("Time,Temperature\n")
        for i, temp_val in enumerate(temps):
            f.write(f"{i},{temp_val}\n")
    print("Temperature data successfully written to temps.csv")
except IOError as e:
    print(f"Error writing to temps.csv: {e}")


try:
    with open("humidity.txt", "w") as f:
        f.write("Time,Humidity\n")
        for i, humidity_val in enumerate(humidity_data):
            f.write(f"{i},{humidity_val}\n")
    print("Humidity data successfully written to humidity.txt")
except IOError as e:
    print(f"Error writing to humidity.txt: {e}")

plt.figure(figsize=(10, 6))
plt.plot(temps, marker='o', linestyle='-', color='red')
plt.xlabel("Time (s)")
plt.ylabel("Temperature (C)")
plt.title("Temperature Log")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(humidity_data, marker='o', linestyle='-', color='blue') 
plt.xlabel("Time (s)")
plt.ylabel("Humidity (%)")
plt.title("Humidity Log")
plt.grid(True) 
plt.show()

