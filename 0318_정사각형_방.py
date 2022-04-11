dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(i,j):
    global cnt
    for k in range(4):
        if 0 <= i+dx[k] <= N-1 and 0 <= j+dy[k] <= N-1:
            if room[i][j] + 1 == room[i+dx[k]][j+dy[k]]:
                cnt += 1
                dfs(i+dx[k],j+dy[k])

for tc in range(int(input())):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    for i in range(N):
        for j in range(N):
            cnt = 1
            dfs(i,j)
            if cnt > max_cnt:
                max_cnt = cnt
                start = room[i][j]
            elif cnt == max_cnt and start > room[i][j]:
                start = room[i][j]
    
    print(f'#{tc+1}',start, max_cnt)