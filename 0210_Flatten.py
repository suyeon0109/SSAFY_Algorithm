for i in range(10):
    n = int(input())
    la = list(map(int, input().split()))


    for k in range(n+1):
        max = 0 
        min = 0
        for j in range(len(la)):
            if j == 0:
                min = la[j]
                max = la[j]
                idx_min = j
                idx_max = j
            else:
                if la[j] <= min:
                    min = la[j]
                    idx_min = j
                if la[j] >= max:
                    max = la[j]
                    idx_max = j

        la[idx_min] += 1
        la[idx_max] -= 1
    
    print(f'#{i+1}',max-min)
    
