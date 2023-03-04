# cook your dish here
t = int(input())

for i in range(t):
    x, y = input().split()
    x, y = int(x), int(y)
    if 100-100*x/100 == 200-200*y/100:
        print("BOTH")
    elif 100-100*x/100 < 200-200*y/100:
        print("FIRST")
    else:
        print("SECOND")
