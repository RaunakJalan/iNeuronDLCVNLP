# Assignment 7: Numpy operations

----------------------------------------------------------------------------------------------------------------------------------

## 1. Write a function so that the columns of the output matrix are powers of the input vector. The order of the powers is determined by the increasing boolean argument. 
##      Specifically, when increasing is False, the i-th output column is the input vector raised element-wise to the power of N - i - 1.


### For input: [1,2,3,4,5] and N=5

### Output

Method 1:

[[  1   1   1   1   1]

 [ 16   8   4   2   1]

 [ 81  27   9   3   1]

 [256  64  16   4   1]

 [625 125  25   5   1]]


Method 2:

[[  1   1   1   1   1]

 [ 16   8   4   2   1]

 [ 81  27   9   3   1]

 [256  64  16   4   1]

 [625 125  25   5   1]]

------------------------------------------------------------------------------------------------------------------------------------

## 2. Calculate Moving average for a given array and a window size greater than 0.

### For input: [3,5,7,2,8,10,11,65,72,81,99,100,150] and windowSize=3

[  5.           4.66666667   5.66666667   6.66666667   9.66666667 28.66666667  49.60333333  78.93666667  90.60333333 116.33333333]
