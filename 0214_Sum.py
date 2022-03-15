for tc in range(10):
    number = int(input())
    la = [list(map(int, input().split())) for _ in range(100)]

    s_max = 0
    for i in range(100):
        tr = 0
        for j in range(100):
            tr += la[i][j]
            if tr > s_max:
                s_max = tr
    
    for k in range(100):
        tl = 0
        for l in range(100):
            tl += la[l][k]
            if tl > s_max:
                s_max = tl
    
    tp = 0
    for p in range(100):
        tp += la[p][p]
    if tp > s_max:
        s_max = tp
    
    ta = 0
    for a in range(100):
        ta += la[a][99-a]
    if ta > s_max:
        s_max = ta
    
    print(f'#{number}',s_max)
