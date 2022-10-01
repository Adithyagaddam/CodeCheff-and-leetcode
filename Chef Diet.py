T = int(input())
for i in range(T):
    N,K = list(map(int,input().split()))
    A = list(map(int,input().split()))
    count = 0
    for i in range(N):
        count += A[i]
        if count >= K:
             count -= K
        else:
            print("NO",i+1)
            count =- 1
            break
    if count >= 0:
        print("YES")
           
