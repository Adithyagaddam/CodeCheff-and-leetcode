import math
for i in range(int(input())):
    a,b=map(int,input().strip().split())
    print(math.gcd(a,b),math.lcm(a,b))
