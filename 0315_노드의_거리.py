def distance():
    Q.append(S)
    visit[S] = 1

    while Q:
        t = Q.pop(0)
        p = visit[t]
        for i in range(V+1):
            if adj[t][i] == 1 and visit[i] == 0:
                if i == G:
                    return p
                visit[i] += p+1
                Q.append(i)
    else:
        return 0

for tc in range(int(input())):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    Q = []

    visit = [0]*(V+1)

    for _ in range(E):
        a,b = map(int, input().split())
        adj[a][b], adj[b][a] = 1,1

    S,G = map(int, input().split())

    print(f'#{tc+1}',distance())