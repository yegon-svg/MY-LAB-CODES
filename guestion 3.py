import random, time
import matplotlib.pyplot as plt

temps = []
humidity_data = [] # Initialize an empty list for humidity data

for t in range(10):
    temp = 25 + random.uniform(-1, 1)
    humidity = random.uniform(40, 60) # Generate random humidity between 40 and 60
    temps.append(temp)
    humidity_data.append(humidity) # Append humidity to the list
    
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

plt.figure(figsize=(10, 6)) # Make the plot a bit larger for better readability
plt.plot(temps, marker='o', linestyle='-', color='red') # Plot temperature with markers and red color
plt.xlabel("Time (s)")
plt.ylabel("Temperature (C)")
plt.title("Temperature Log")
plt.grid(True) # Add a grid for better readability
plt.show()

plt.figure(figsize=(10, 6)) # Create a new figure for humidity
plt.plot(humidity_data, marker='o', linestyle='-', color='blue') # Plot humidity with markers and blue color
plt.xlabel("Time (s)")
plt.ylabel("Humidity (%)")
plt.title("Humidity Log")
plt.grid(True) # Add a grid for better readability
plt.show()
