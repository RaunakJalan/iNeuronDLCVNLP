import pandas as pd
import numpy as np


def fillMissing(FlightNumber):
	bool_data = list(FlightNumber.isna())
	dup_data = list(FlightNumber)
	i = 0
	n = len(bool_data)
	while i < n:
		if bool_data[i] == False:
			break
		i+=1
	point = i
	for fill in range(i-1,-1,-1):
		# print(fill)
		if bool_data[fill]==True:
			dup_data[fill] = dup_data[fill+1]-10
	for fill in range(i+1,n):
		# print(fill)
		if bool_data[fill] == True:
			dup_data[fill] = dup_data[fill-1]+10

	return dup_data

data = {
	'From_To':['LoNDon_paris', 'MAdrid_miLAN','londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
	'FlightNumber':[np.nan, np.nan, 10065, np.nan, np.nan],
	'RecentDelays':[[23, 47], [], [24,43,87], [13], [67, 32]],
	'Airline': ['KLM(!)', '<Air France>(12)', '(British Airways. )', '12. Air France', '''Swiss Air''']
}

df = pd.DataFrame(data)

#print(type(df['FlightNumber']))
df['FlightNumber'] = fillMissing(df['FlightNumber'])
print(df)
