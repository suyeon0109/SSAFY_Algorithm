from collections import deque

for tc in range(10):

    L, S = map(int, input().split())
    called = list(map(int, input().split()))
    adj = [[] for _ in range(max(called)+1)]
    for i in range(0,L,2):
        adj[called[i]].append(called[i+1])

    Q = deque()
    visited = [0] * (max(called)+1)
    Q.append(S)
    visited[S] = 1
    dic = {1:[S]}
    while Q:
        t = Q.popleft()
        n = visited[t]
        for i in adj[t]:
            if visited[i] == 0:
                Q.append(i)
                visited[i] = n + 1
                try:
                    dic[n+1].append(i)
                except:
                    dic[n+1] = [i]

    print(f'#{tc+1}',max(dic[max(dic)]))