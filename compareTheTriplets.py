#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    newArray = []
    x=0
    y=0
    
    for index in range(0, len(a)):
        if a[index] > b[index]:
            x = x+1
            
        elif b[index] > a[index]:
            y = y+1
            
        else:
            continue
        
    newArray.append(x)
    newArray.append(y)
    
    return newArray

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()