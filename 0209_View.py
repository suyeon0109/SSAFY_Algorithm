for i in range(10):
    n = int(input())
    la = list(map(int, input().split()))
    count = 0

    for j in range(2,len(la)-2):
        for k in range(la[j]):
            if la[j]-k > la[j-1] and la[j]-k > la[j-2] and la[j]-k > la[j+1] and la[j]-k > la[j+2]:
                count += 1
            else:
                break
    
    print(f'#{i+1}',count)
