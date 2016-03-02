#may need to install matplotlib and pyephem as dependencies; the pip names for these packages
#are "matplotlib" and "ephem."

import thermsat
import matplotlib.pyplot as plt

sat = thermsat.thermsat.fromfile('sat.cfg')
data = []

dt = 1      #time step (s)

for i in range(24*3600):
    sat.step(dt)
    data.append(sat.temp)

plt.plot(data)
plt.xlabel('Time (s)')
plt.ylabel('Temp (K)')
plt.title('Temp change of CubeSat in ISS orbit vs. time')
plt.show()
