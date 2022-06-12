"""Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(n, arr):
    # Write your code here
    minsum = 0
    maxsum = 0

    arr.sort()
    for i in range(0,n-1):
        minsum += arr[i]
    
    
    arr.sort(reverse=True)
    for j in range(0,n-1):
        maxsum += arr[j]
        
    print(minsum, maxsum)
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    n = len(arr)
    
    miniMaxSum(n, arr)
