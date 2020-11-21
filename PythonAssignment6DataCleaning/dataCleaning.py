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

def strStandard(val):
	val = val.apply(lambda x:x.title())
	return val



data = {
	'From_To':['LoNDon_paris', 'MAdrid_miLAN','londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
	'FlightNumber':[np.nan, np.nan, 10065, np.nan, np.nan],
	'RecentDelays':[[23, 47], [], [24,43,87], [13], [67, 32]],
	'Airline': ['KLM(!)', '<Air France>(12)', '(British Airways. )', '12. Air France', '''Swiss Air''']
}

df = pd.DataFrame(data)

#print(type(df['FlightNumber']))
#1. 
df['FlightNumber'] = fillMissing(df['FlightNumber'])
#print(df)

#2.
fromto = list(df['From_To'])
fromtoSplit = [x.split('_') for x in fromto]
fromLoc, toLoc = [x[0] for x in fromtoSplit], [x[1] for x in fromtoSplit]
temp_df = pd.DataFrame({'From':fromLoc, 'To': toLoc})
#print(temp_df)




#3.
temp_df = temp_df.apply(strStandard)
#print(temp_df)

#4.
#print(df)
df.drop('From_To', inplace=True, axis=1)
final_df = pd.concat([temp_df, df], axis=1, sort = False)
#print(final_df)














