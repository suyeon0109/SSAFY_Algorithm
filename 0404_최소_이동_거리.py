def bfs():
    while Q:
        t = Q.pop(0)
        for i in range(N+1):
            if adj[t][i]:
                if visited[i] > adj[t][i] + visited[t]:
                    visited[i] = adj[t][i] + visited[t]
                    Q.append(i)

for tc in range(int(input())):
    N, E = map(int, input().split())
    adj = [[0]*(N+1) for _ in range(N+1)]
    Q = []
    visited = [10*N]*(N+1)

    for _ in range(E):
        s,e,w = map(int, input().split())
        adj[s][e] = w
    Q.append(0)
    visited[0] = 0
    bfs()
    print(f'#{tc+1}',visited[N])