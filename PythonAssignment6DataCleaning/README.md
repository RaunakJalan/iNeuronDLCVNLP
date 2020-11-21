# Original Data

| From_To          	| FlightNumber 	| RecentDelays 	| Airline             	|
|------------------	|--------------	|--------------	|---------------------	|
| LoNDon_paris     	| NaN          	| [23, 47]     	| KLM(!)              	|
| MAdrid_miLAN     	| NaN          	| []           	| (12)                	|
| londON_StockhOlm 	| 10065.0      	| [24, 43, 87] 	| (British Airways. ) 	|
| Budapest_PaRis   	| NaN          	| [13]         	| 12. Air France      	|
| Brussels_londOn  	| NaN          	| [67, 32]     	| Swiss Air           	|

# After first operation: Replacing NAN flight numbers

| From_To          	| FlightNumber 	| RecentDelays 	| Airline             	|
|------------------	|--------------	|--------------	|---------------------	|
| LoNDon_paris     	| 10045.0      	| [23, 47]     	| KLM(!)              	|
| MAdrid_miLAN     	| 10055.0      	| []           	| (12)                	|
| londON_StockhOlm 	| 10065.0      	| [24, 43, 87] 	| (British Airways. ) 	|
| Budapest_PaRis   	| 10075.0      	| [13]         	| 12. Air France      	|
| Brussels_londOn  	| 10085.0      	| [67, 32]     	| Swiss Air           	|

# After Second Operation: Separating From_To in two different columns

| From     	| To        	|
|----------	|-----------	|
| LoNDon   	| paris     	|
| MAdrid   	| miLAN     	|
| londON   	| StockhOlm 	|
| Budapest 	| PaRis     	|
| Brussels 	| londOn    	|

# After Third Operation: Formatting of strings in From and Two columns

| From     	| To        	|
|----------	|-----------	|
| London   	| Paris     	|
| Madrid   	| Milan     	|
| London   	| Stockholm 	|
| Budapest 	| Paris     	|
| Brussels 	| London    	|

# After Fourth Operation: Dropping From_To from original dataframe and concatenating temp_df with From and Two columns

| From     	| To        	| FlightNumber 	| RecentDelays 	| Airline             	|
|----------	|-----------	|--------------	|--------------	|---------------------	|
| London   	| Paris     	| 10045.0      	| [23, 47]     	| KLM(!)              	|
| Madrid   	| Milan     	| 10055.0      	| []           	| (12)                	|
| London   	| Stockholm 	| 10065.0      	| [24, 43, 87] 	| (British Airways. ) 	|
| Budapest 	| Paris     	| 10075.0      	| [13]         	| 12. Air France      	|
| Brussels 	| London    	| 10085.0      	| [67, 32]     	| Swiss Air           	|

# After Fifth Operation: Expanding RecentDelays into Delay1, Delay2 ... and then dropping RecentDelays

| From     	| To        	| FlightNumber 	| Delay1 	| Delay2 	| Delay3 	|
|----------	|-----------	|--------------	|--------	|--------	|--------	|
| London   	| Paris     	| 10045.0      	| 23.0   	| 47.0   	| NaN    	|
| Madrid   	| Milan     	| 10055.0      	| NaN    	| NaN    	| NaN    	|
| London   	| Stockholm 	| 10065.0      	| 24.0   	| 43.0   	| 87.0   	|
| Budapest 	| Paris     	| 10075.0      	| 13.0   	| NaN    	| NaN    	|
| Brussels 	| London    	| 10085.0      	| 67.0   	| 32.0   	| NaN    	|

[5 rows x 7 columns]


# Thank You
