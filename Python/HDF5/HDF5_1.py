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

import h5py

f = h5py.File("weather.hdf5", "w")
f["/15/temperature"] = temperature
f["/15/temperature"].attrs["dt"] = 10.0
f["/15/temperature"].attrs["start_time"] = 1475204299
f["/15/wind"] = wind
f["/15/wind"].attrs["dt"] = 5.0

dataset = f["/15/temperature"]
for key, value in dataset.attrs.items():