n=int(input())
for i in range(n):
    a,b=map(int,input().split(' '))
    list1=[]
    for i in range(a):
        d=list(map(int,input().split()))
        if d[2]<=b:
            list1.append(d[0]*d[1]) 
    if len(list1)==0:
        print("no tablet")
    else:
        print(max(list1))
