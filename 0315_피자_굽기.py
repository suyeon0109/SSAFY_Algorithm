from collections import deque
for tc in range(int(input())):
    N, M = map(int, input().split())
    piz = [i for i in range(1,M+1)]
    la = list(map(int, input().split()))
    da = {}

    for i in range(len(la)):
        da[i+1] = la[i]

    Q = deque()
    for _ in range(N):
        Q.append(piz.pop(0))

    while sum(Q) != 0:

        if Q[0] != 0:
            a = Q.popleft()

            if da[a]//2 == 0:
                da[a] //=2
                try:
                    Q.appendleft(piz.pop(0))
                except:
                    Q.appendleft(0)
            else:
                Q.appendleft(a)
                da[a] //=2

        Q.rotate(-1)
    
    print(f'#{tc+1}', a)