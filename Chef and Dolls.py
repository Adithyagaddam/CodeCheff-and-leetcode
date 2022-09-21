n=int(input())
for i in range(n):
    s=int(input())
    list1=[]
    for i in range(s):
        k=int(input())
        list1.append(k)
    for i in range(len(list1)):
        if list1.count(list1[i])%2!=0:
            print(list1[i])
            break
