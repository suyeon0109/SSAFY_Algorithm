def tree(n):
    if n <= N:
        if not val[n]:
            return tree(2*n) + tree(2*n+1)
        else:
            return val[n]
    return 0

for tc in range(int(input())):
    N, M, L = map(int, input().split())
    val = [0]*(N+1)
    for _ in range(M):
        a,b = map(int, input().split())
        val[a] = b

    print(f'#{tc+1}',tree(L))