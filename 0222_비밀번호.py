for tc in range(10):
    n, m = map(str, input().split())
    la = []
    for i in range(len(m)):
        if not la:
            la.append(m[i])
        else:
            if la[-1] == m[i]:
                la.pop()
            else:
                la.append(m[i])
    
    print(f'#{tc+1}',''.join(la))