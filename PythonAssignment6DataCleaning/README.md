# Original Data

            From_To  FlightNumber  RecentDelays              Airline
0      LoNDon_paris           NaN      [23, 47]               KLM(!)
1      MAdrid_miLAN           NaN            []     <Air France>(12)
2  londON_StockhOlm       10065.0  [24, 43, 87]  (British Airways. )
3    Budapest_PaRis           NaN          [13]       12. Air France
4   Brussels_londOn           NaN      [67, 32]            Swiss Air

# After first operation: Replacing NAN flight numbers

            From_To  FlightNumber  RecentDelays              Airline
0      LoNDon_paris       10045.0      [23, 47]               KLM(!)
1      MAdrid_miLAN       10055.0            []     <Air France>(12)
2  londON_StockhOlm       10065.0  [24, 43, 87]  (British Airways. )
3    Budapest_PaRis       10075.0          [13]       12. Air France
4   Brussels_londOn       10085.0      [67, 32]            Swiss Air

# After Second Operation: Separating From_To in two different columns

       From         To
0    LoNDon      paris
1    MAdrid      miLAN
2    londON  StockhOlm
3  Budapest      PaRis
4  Brussels     londOn

# After Third Operation: Formatting of strings in From and Two columns

       From         To
0    London      Paris
1    Madrid      Milan
2    London  Stockholm
3  Budapest      Paris
4  Brussels     London

# After Fourth Operation: Dropping From_To from original dataframe and concatenating temp_df with From and Two columns

       From         To  FlightNumber  RecentDelays              Airline
0    London      Paris       10045.0      [23, 47]               KLM(!)
1    Madrid      Milan       10055.0            []     <Air France>(12)
2    London  Stockholm       10065.0  [24, 43, 87]  (British Airways. )
3  Budapest      Paris       10075.0          [13]       12. Air France
4  Brussels     London       10085.0      [67, 32]            Swiss Air

# After Fifth Operation: Expanding RecentDelays into Delay1, Delay2 ... and then dropping RecentDelays

       From         To  FlightNumber   Delay1  Delay2  Delay3
0    London      Paris       10045.0     23.0    47.0     NaN
1    Madrid      Milan       10055.0      NaN     NaN     NaN
2    London  Stockholm       10065.0     24.0    43.0    87.0
3  Budapest      Paris       10075.0     13.0     NaN     NaN
4  Brussels     London       10085.0     67.0    32.0     NaN

[5 rows x 7 columns]


# Thank You
