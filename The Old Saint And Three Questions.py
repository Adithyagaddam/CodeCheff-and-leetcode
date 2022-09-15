n=int(input())
for i in range(n):
    a=list(map(int,input().split(' ')))
    b=list(map(int,input().split(' ')))
    count=a.count(1)
    suma=b.count(1)
    if count==suma:
       print("Pass")
    else:
       print("Fail")
