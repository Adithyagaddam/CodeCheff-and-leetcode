import math
for i in range(int(input())):
    a,b=map(int,input().strip().split())
    print(math.ceil((a*b)/4))
