for i in range(int(input())):
    N = int(input())
    la = [[0]* N for _ in range(N)]

    x,y = 0,-1
    cnt = 0
    j = 0

    while N != 0:

        for k in range(1,N+1):
            cnt +=1
            y += (-1)**j
            la[x][y] = cnt

        for m in range(1,N):
            cnt += 1
            x += (-1)**j
            la[x][y] = cnt

        j += 1
        N -= 1

    print(f'#{i+1}')
    for p in range(len(la)):
        print(*la[p])