for n in range(int(input())):
    N, K = map(int, input().split())
    la = list(map(int, input().split()))
    ans = 0

    for i in range(2 ** N):
        sum = 0
        for j in range(N):
            if i & (1<<j):
                sum += la[j]

        if sum == K:
            ans += 1
    print(f'#{n+1}',ans)
