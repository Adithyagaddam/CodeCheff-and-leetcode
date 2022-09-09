n=int(input())
for i in range(n):
    a,b=map(int,input().split(' '))
    s=b*(b+1)/2
    if a>=s:
        print("YES")
    else:
        print("NO")
