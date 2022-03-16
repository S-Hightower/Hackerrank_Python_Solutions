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

def miniMaxSum(arr):
    arr.sort()
    
    hold = [None] * int(len(arr)-3)
    
    for index in range(0, len(arr)-3):
        temp = 0
        for index2 in range(index, index+4):
            temp = temp+arr[index2]
        hold[index] = temp
        
    print(hold[0], hold[-1])

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)