import math
n=int(input())
for i in range(n):
    a,b=map(int,input().strip().split())
    k=(a*6)/2
    s=(b*6)/3
    if k<=s:
        print(int(k))
    else:print(int(s))
    
