import math
for i in range(int(input())):
    a,b,c=map(int,input().strip().split())
    s=math.ceil(b/c)
    print(a*s)
