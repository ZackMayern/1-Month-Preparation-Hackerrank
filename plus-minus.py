"""Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(n, arr):
    # Write your code here
    positivecounter = 0
    negativecounter = 0
    zerocounter = 0
    
    for i in range(n):
        if arr[i]==0:
            zerocounter+=1
        elif arr[i]>0:
            positivecounter+=1
        else:
            negativecounter+=1
    
    print("%.6f"%(positivecounter/n))
    print("%.6f"%(negativecounter/n))
    print("%.6f"%(zerocounter/n))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(n, arr)
