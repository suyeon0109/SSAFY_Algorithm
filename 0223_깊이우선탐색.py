for tc in range(int(input())):
    V, E = map(int, input().split())
    edge = [[] for _ in range(V+1)]
    stk = [0]
    path = []

    for _ in range(E):
        a,b = map(int, input().split())
        edge[b].append(a)
        edge[b].sort()
        edge[a].append(b)
        edge[a].sort()

    loc = 1
    stk.append(loc)
    path.append(loc)
    while len(path) != V:
        for i in range(len(edge[loc])):
            if edge[loc][i] in path:
                pass
            else:
                loc = edge[loc][i]
                stk.append(loc)
                path.append(loc)
                break
        else:
            stk.pop()
            loc = stk[-1]
    
    print(f'#{tc+1}',*path)