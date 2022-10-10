for _ in range(int(input())):
    ll=int(input())
    s=input()
    s=s.replace(".","")
    s=s.replace("HT","")
    if len(s)!=0:
        print("Invalid")
    else:
        print("Valid")
