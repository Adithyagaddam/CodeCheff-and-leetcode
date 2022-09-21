n=int(input())
for i in range(n):
    list1=[]
    a=list(map(int,input().split()))
    for i in range(5):
        if a[i]==1:
            list1.append(a)
    if len(list1)==0:
        print("Beginner")
    elif len(list1)==1:
        print("Junior Developer")
    elif len(list1)==2:
        print("Middle Developer")
    elif len(list1)==3:
        print("Senior Developer")
    elif len(list1)==4:
        print("Hacker")
    else:
        print("Jeff Dean")
