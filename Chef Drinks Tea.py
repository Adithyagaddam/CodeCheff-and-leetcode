import math
for i in range(int(input())):
    a,b,c=map(int,input().strip().split())
    print(math.ceil(a/b)*c)
