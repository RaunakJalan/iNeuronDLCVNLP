import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import optimize

def yearly_temps(times, avg, ampl, time_offset):
	return (avg + ampl * np.cos((times + time_offset) * 2 * np.pi / times.max()))

months = np.arange(12)
days = np.linspace(0, 12, num=365)

temp_max = [39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25]
temp_min = [21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18]

# print(stats.describe(temp_max))
# print(stats.describe(temp_min))


res_max, cov_max = optimize.curve_fit(yearly_temps, months, temp_max, [20, 10, 0])
res_min, cov_min = optimize.curve_fit(yearly_temps, months, temp_min, [-40, 20, 0])

plt.figure()
plt.plot(months, temp_max, 'ro')
plt.plot(days, yearly_temps(days, *res_max), 'r-')
plt.plot(months, temp_min, 'bo')
plt.plot(days, yearly_temps(days, *res_min), 'b-')
plt.xlabel('Month')
plt.ylabel('Temperature ($^\circ$C)')

plt.show()
