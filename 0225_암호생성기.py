for tc in range(10):
    n = int(input())
    Q = list(map(int, input().split()))
    m = 1
    while 1:
        t = Q.pop(0)
        if t-m<=0:
            Q.append(0)
            break
        else:
            Q.append(t-m)
        m += 1
        if m == 6:
            m = 1
    print(f'#{n}',*Q)