def tree(n):
    if n:
        lb.append(n)
        tree(lf[n])
        tree(rt[n])

for tc in range(int(input())):
    V = int(input())
    la = list(map(int, input().split()))
    lf = [0]*(V+1)
    rt = [0]*(V+1)
    lb = []
    for i in range(0,len(la),2):
        if lf[la[i]] == 0:
            lf[la[i]] = la[i+1]
        else:
            rt[la[i]] = la[i+1]
    tree(1)
    print(f'#{tc+1}',*lb)