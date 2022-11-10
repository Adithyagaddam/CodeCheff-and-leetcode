import math
from math import sqrt
for i in range(int(input())):
    a,b,c,d=map(int,input().strip().split())
    if a<=sqrt(b**2+(2*c*d)):
        print("Yes")
    else:
        print("No")
    
