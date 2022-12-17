for i in range(int(input())):
    s=int(input())
    if s<3:
        print("LIGHT")
    elif s>=3 and s<7:
        print("MODERATE")
    else:print("HEAVY")
