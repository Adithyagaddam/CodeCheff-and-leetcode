n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    if a>=b and a<=c:
        print("Take second dose now")
    elif a<b and a<c:
        print("Too Early")
    else:
        print("Too Late")
