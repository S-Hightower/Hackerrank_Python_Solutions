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

def plusMinus(arr):
    pos = 0
    neg = 0
    zed = 0
    
    for index in range (0, len(arr)):
        
        if arr[index] > 0:
            pos = pos + 1
            
        elif arr[index] < 0:
            neg = neg + 1
            
        else:
            zed = zed + 1
            
    print(pos/len(arr))
    print(neg/len(arr))
    print(zed/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)