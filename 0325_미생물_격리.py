dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

for tc in range(int(input())):
    N, M, K = map(int, input().split())
    cell = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        a,b,c,d = map(int, input().split())
        cell[a][b].append((c,d))
    
    for _ in range(M):

        cell_1hour = [[[] for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if cell[i][j] :
                    k = cell[i][j][0][1]
                    cell_1hour[i + dx[k]][j + dy[k]].append(cell[i][j][0])

                    if i + dx[k] == 0 or i + dx[k] == N-1 or j + dy[k] == 0 or j + dy[k] == N-1:
                        num, dir = cell_1hour[i + dx[k]][j + dy[k]][0]
                        num //=2
                        if dir%2 == 0:
                            dir -= 1
                        else:
                            dir += 1
                        cell_1hour[i + dx[k]][j + dy[k]] = [(num, dir)]
        
        for i in range(N):
            for j in range(N):
                if len(cell_1hour[i][j]) > 1:
                    cell_1hour[i][j].sort()
                    p = 0
                    for s in cell_1hour[i][j]:
                        p += s[0]
                    q = cell_1hour[i][j][-1][1]
                    cell_1hour[i][j] = [(p,q)]

        cell = cell_1hour
    
    sum_num = 0
    for m in range(N):
        for n in range(N):
            if cell[m][n]:
                sum_num += cell[m][n][0][0]

    print(f'#{tc+1}', sum_num)