for i in range(int(input())):
    n = int(input())
    la = list(map(int, input().split()))

    for j in range(n):
        for k in range(len(la)-1):
            if la[k] > la[k+1]:
                la[k], la[k+1] = la[k+1], la[k]
    
    print(f'#{i+1}',la[-1]-la[0])