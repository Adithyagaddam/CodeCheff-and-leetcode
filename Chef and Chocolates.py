n=int(input())
for i in range(n):
    a,b,c=map(int,input().strip().split())
    k=a*5+b*10
    print(int(k/c))
