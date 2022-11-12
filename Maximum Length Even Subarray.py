for i in range(int(input())):
    a=int(input())
    if ((((a * (a + 1)) / 2) % 2) == 0):
        print(a)
    else:
        print(a-1)
