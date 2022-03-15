for i in range(int(input())):
    K, N, M = map(int, input().split())
    la = list(map(int, input().split()))

    d = 0
    count = 0
    charge = 0
    
    for _ in range(1000):
        for j in range(K,-1,-1):
            if j == 0:
                charge = 0
                break
            if d + j >= N:
                break
            if d + j in la:
                d = d + j
                charge += 1
                break

    print(f'#{i+1}',charge)