def tree(n):
    global cnt
    if n:
        tree(lf[n])
        cnt += 1
        tree(rt[n])

for tc in range(int(input())):
    E, N = map(int, input().split())
    la = list(map(int, input().split()))
    V = max(la)
    lf = [0]*(V+1)
    rt = [0]*(V+1)
    cnt = 0
    for i in range(0,len(la),2):
        if not lf[la[i]]:
            lf[la[i]] = la[i+1]
        else:
            rt[la[i]] = la[i+1]
    
    tree(N)

    print(f'#{tc+1}',cnt)