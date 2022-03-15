for tc in range(int(input())):
    m = input()
    la = []
    for i in range(len(m)):
        if not la:
            la.append(m[i])
        else:
            if la[-1] == m[i]:
                la.pop()
            else:
                la.append(m[i])
    
    print(f'#{tc+1}',len(la))