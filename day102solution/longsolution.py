import math

def mean(a):
    l = len(a)
    
    return sum([entry for entry in a])/len(a)
    

def unit(a):
    a = [entry - mean(a) for entry in a]
    b = sum([entry ** 2 for entry in a])
    if b == 0: return [0 for entry in a]
    b = math.sqrt(b)
    a = [entry/b for entry in a]
    return a

def dot(a, b):
    len_a = len(a)
    len_b = len(b)
    
    return sum([a[i] * b[i] for i in range(len_a)])

count = int(input())

for i in range(count):
    student_size = int(input())
    gpas = input().strip().split()
    gpas = [float(entry) for entry in gpas]
    gpas = unit(gpas)
    tests = []
    for j in range(5):
        test = input().strip().split()
        test = [float(entry) for entry in test]
        test = unit(test)
        score = dot(gpas, test)
        tests.append(score)
        
    print(tests.index(max(tests)) + 1)
