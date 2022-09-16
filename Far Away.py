n=int(input())
for i in range(n):
    a,b=map(int,input().split(' '))
    s=list(map(int,input().split(' ')))
    con=0
    for i in range(a):
        if s[i] <= int(b/2):
            con+=abs(s[i]-b)
        else:
            con+=abs(s[i]-1)
    print(con)
        
        
