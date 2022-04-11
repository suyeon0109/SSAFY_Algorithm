from collections import deque
import sys

def dfs(lst):
    global p, sum_min
    if sum(stk) > sum_min:
        p -= 1
        return
    for k in range(N):
        if visited[k] == 0:
            visited[k] = 1
            stk.append(lst[k])
            if p == N-1:
                p -= 1
                if sum_min > sum(stk):
                    sum_min = sum(stk)
                stk.pop()
                visited[k] = 0
                return
            p += 1
            dfs(la[p])
            visited[k] = 0
            stk.pop()
    else:
        p -= 1

for tc in range(int(input())):
    stk = deque()
    N = int(input())
    la = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    visited = [0] * N
    sum_min = 9 * N
    p = 0
    dfs(la[p])
    print(f'#{tc+1}', sum_min)