#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s  starting point of Sam's house location
#  2. INTEGER t  ending location of Sam's house location
#  3. INTEGER a   location of the Apple tree
#  4. INTEGER b  location of the Orange tree
#  5. INTEGER_ARRAY apples  distances at which each apple falls from the tree
#  6. INTEGER_ARRAY oranges  distances at which each orange falls from the tree
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    print(sum([1 for x in apples if (x+a) >= s and (x+a) <= t]))
    print(sum([1 for x in oranges if (x+b) >= s and (x+b) <= t]))
            
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)