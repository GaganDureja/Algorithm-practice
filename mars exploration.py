#Link: https://www.hackerrank.com/challenges/mars-exploration/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    multiplier = len(s)//3
    res = 'SOS'*multiplier  
    return sum(res[x]!=s[x] for x in range(len(res)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
