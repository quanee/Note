import numpy as np

temperature = np.random.random(1024)
print(temperature)

dt = 10
start_time = 1475204299
station = 15
np.savez("weather.npz", data=temperature, start_time=start_time, station=station)

out = np.load("weather.npz")

print(out["data"])
print(out["start_time"])
print(out["station"])

wind = np.random.random(2048)
dt_wind = 5.0