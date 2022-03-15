def DFS(s, N):
    visited = [0] * N
    stk = []
    stk.append(s)
    visited[s] = 1
    sol.append(s)
    while stk:
        for d in range(0, N):
            if visited[d] == 0 and adj[s][d]:
                stk.append(s)
                visited[d] = 1
                sol.append(d)
                s = d
                break
        else:
            s = stk.pop()
        if 99 in sol:
            break

for tc in range(10):
    
    N, E = map(int, input().split())
    adj = [[0] * (99 + 1) for _ in range(99 + 1)]
    sol = []
    m = list(map(int,input().split()))
    for i in range(0, len(m)-1,2):
        adj[m[i]][m[i+1]] = 1
    DFS(0, 99 + 1)
    if 99 in sol:
        print(f'#{tc+1}', 1)
    else:
        print(f'#{tc+1}', 0)