#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    
    for c in range(len(arr)//2):
        arr[c][1]="-" 
    arr.sort(key= lambda num:int(num[0]))
    for word in arr:
        print(word[1], end=" ")

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
