for i in range(int(input())):
    a=int(input())
    s=input()
    k=[x for x in s]
    p=[]
    for i in range(a):
        if k[i]=="A":
            p.append("T")
        elif k[i]=="T":
            p.append("A")
        elif k[i]=="C":
            p.append("G")
        else:
            p.append("C")
    print(''.join(p))
