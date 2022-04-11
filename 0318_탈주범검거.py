from collections import deque

# 각 파이프 번호당 이동할 수 있는 방향 설정
dic = {
    1:[(-1,0),(0,1),(1,0),(0,-1)], 
    2:[(-1,0), (1,0)], 
    3:[(0,1),(0,-1)], 
    4:[(-1,0),(0,1)], 
    5:[(0,1),(1,0)], 
    6:[(0,-1),(1,0)],
    7:[(-1,0),(0,-1)]
    }

for tc in range(int(input())):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    Q = deque()
    Q.append((R,C))
    visited[R][C] = 1
    
    while Q:
        a,b = Q.popleft()
        n = visited[a][b]

        # 현재위치의 파이프 번호를 딕셔너리에서 호출 -> 갈 수 있는 방향 설정됨(d)
        for d in dic[tunnel[a][b]]:
            dx = a+d[0]
            dy = b+d[1]

            # 이동할 방향에 따라 유효한 파이프를 제한. ex) 윗방향 -> 1,2,5,6번 파이프만 가능
            if d == (-1,0):
                lst = [1,2,5,6]
            elif d == (0,1):
                lst = [1,3,6,7]
            elif d == (1,0):
                lst = [1,2,4,7]
            else:
                lst = [1,3,4,5]
                
            # 한칸씩 이동하면서 해당 이동위치에 몇시간이 지났는지 기록. 설정시간 L에 도달하면 append 멈춘다.
            if 0 <= dx <= N-1 and 0 <= dy <= M-1 and visited[dx][dy] == 0 and tunnel[dx][dy] in lst:
                if n+1 <= L:
                    visited[dx][dy] = n+1
                    Q.append((dx,dy))

    # visited 이차원 배열에서 방문한적 없는 곳의 갯수를 세서, 전체 칸수에서 빼준다.
    cnt_0 = 0
    for i in visited:
        cnt_0 += i.count(0)

    print(f'#{tc+1}', N*M - cnt_0)