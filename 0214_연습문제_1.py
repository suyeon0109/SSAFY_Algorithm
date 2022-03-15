dx = [0,1,0,-1]
dy = [1,0,-1,0]

for p in range(int(input())):
    n = int(input())
    la=[list(map(int,input().split())) for _ in range(n)]

    s = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                try:
                    if i+dx[k]<0 or j+dy[k]<0:
                        pass
                    else:
                        s += abs(la[i][j] - la[i+dx[k]][j+dy[k]])
                except:
                    pass
    
    print(f'#{p+1}',s)
