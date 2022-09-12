n=int(input())
for i in range(n):
    a=list(map(int,input().split(' ')))
    s=a[0]+a[1]+a[2]
    p=a[3]+a[4]+a[5]
    if s>p:
        print("1")
    elif p>s:
        print("2")
