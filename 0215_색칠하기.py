for i in range(int(input())):
    la = [[0]*10 for _ in range(10)]
    lb = [[0]*10 for _ in range(10)]

    n = int(input())
    for p in range(n):
        lc = list(map(int, input().split()))

        for j in range(lc[0],lc[2]+1):
            for k in range(lc[1],lc[3]+1):

                if lc[-1] == 1:
                    la[j][k] += 1
                else:
                    lb[j][k] += 1

    cnt = 0
    for q in range(10):
        for w in range(10):
            if la[q][w] != 0 and lb[q][w] != 0:
                cnt += 1
    print(f'#{i+1}',cnt)