import math
n=int(input())
for i in range(n):
    a,b=map(int,input().strip().split())
    print(math.floor(a/b)+a%b)
