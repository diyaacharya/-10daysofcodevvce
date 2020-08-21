newarr=[]
for _ in range(int(input())):
    items = list(map(int,input().split()))
    if(items[0] is 1):
        newarr.append(items[1])
    elif(items[0] is 2):
        newarr.pop(0)
    else:
        print (newarr[0])