from scipy.stats import spearmanr

t = int(input())
for i in range(t):
    n = int(input())
    gpa = [float(j) for j in input().split()]
    nearer_value = 0.0
    nearer_valuetest = None
    for k in range(5):
        exams = [float(j) for j in input().split()]
        cor,p = spearmanr(gpa, exams)
        if cor > nearer_value :
            nearer_value = cor
            nearer_valuetest = k + 1
    print(nearer_valuetest)