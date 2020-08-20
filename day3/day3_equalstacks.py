#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    st1, st2, st3 =map(sum, (h1, h2, h3))
    while h1 and h2 and h3:
        m = min(st1, st2, st3)
        while st1 > m: 
            st1 -= h1.pop(0)
        while st2 > m: 
            st2 -= h2.pop(0)
        while st3 > m: 
            st3 -= h3.pop(0)
        if st1 == st2 == st3: 
            return st1
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
