def tree(n):
    if n:
        tree(lf[n])
        lb.append(dic[n])
        tree(rt[n])


for tc in range(10):
    V = int(input())
    lf = [0]*(V+1)
    rt = [0]*(V+1)
    dic = {}
    for i in range(1,V+1):
        la = list(map(str, input().split()))
        dic[i] = la[1]
        la.pop(0)
        la.pop(0)
        if len(la) == 2:
            lf[i] = int(la[0])
            rt[i] = int(la[1])
        elif len(la) == 1:
            lf[i] = int(la[0])

    lb = []

    tree(1)
    print(f'#{tc+1}',''.join(lb))