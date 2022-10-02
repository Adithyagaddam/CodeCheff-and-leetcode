n=int(input())
for i in range(n):
    a,b=map(int,input().split(' '))
    i=1
    counta=0
    countb=0
    while True:
        j=i+1
        countb+=j
        counta+=i
        i+=2
        if counta>a:
            print("Bob")
            break
        elif countb>b:
            print("Limak")
            break
