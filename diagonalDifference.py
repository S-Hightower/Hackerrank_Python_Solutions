#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    diagOne = 0
    diagTwo = 0
    
    for index in range(0, len(arr)):
        diagOne = diagOne + arr[index][index]
        
    for index2 in range(0, len(arr)):
        diagTwo = diagTwo + arr[index2][len(arr)-1-index2]
        
    return abs(diagOne - diagTwo)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()