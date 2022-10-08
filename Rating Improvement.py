n=int(input())
for i in range(n):
    a,b=map(int,input().split(' '))
    if b in range(a,a+201):
        print("YES")
    else:
        print('NO')
