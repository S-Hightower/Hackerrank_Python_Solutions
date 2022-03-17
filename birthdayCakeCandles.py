#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    tallestNum = 0
    temp = candles[0]
    
    for index in range(1, len(candles)):
        if candles[index] > temp:
            temp = candles[index]
            
    for index in range(0, len(candles)):
        if candles[index] == temp:
            tallestNum = tallestNum + 1
            
    return tallestNum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()