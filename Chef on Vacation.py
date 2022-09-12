for _ in range(int(input())):
    a=list(map(int,input().split(' ')))
    c=a[0]+a[1]
    if c<=a[2]:
        print("YES")
    else:
        print("NO")
