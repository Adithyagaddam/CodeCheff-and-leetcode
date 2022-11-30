import math
for i in range(int(input())):
    a,b=map(int,input().strip().split())
    s=math.ceil(a/6)
    print(s*b)
