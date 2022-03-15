from collections import deque
for tc in range(int(input())):
    N, M = map(int, input().split())
    la = list(map(int, input().split()))
    Q = deque()
    for _ in range(N):
        Q.appendleft(la.pop(0))

    a = Q.popleft()
    if a//2 == 0:
        try:
            Q.appendleft(la.pop(0))
        except:
            Q.appendleft(0)
    else:
        Q.appendleft(a//2)
        Q.rotate(1)

    Q.append(a//2)