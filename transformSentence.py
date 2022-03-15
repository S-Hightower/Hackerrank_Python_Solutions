#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    letters = sentence.split()
    
    newList=[]
    spot=""
    
    for index in letters:
        spot+=index[0]
        
        for index2 in range(0, len(index)-1):
            
            if (index[index2].lower() < index[index2+1].lower()):
                spot+=(index[index2+1].upper())
                
            elif (index[index2].lower() > index[index2+1].lower()):
                spot+=(index[index2+1].lower())
                
            else:
                spot+=index[index2+1]
                
        newList.append(spot)
        spot=""
    result=""
    
    for indi in newList:
        result = result+" "+indi
    return (result.strip())
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()