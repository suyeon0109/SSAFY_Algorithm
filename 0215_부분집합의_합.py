for n in range(int(input())):
    la = [k for k in range(1,13)]
    N, K = map(int, input().split())
    ans = 0

    for i in range(2 ** 12):
        sum = 0
        cnt = 0
        for j in range(12):
            if i & (1<<j):
                sum += la[j]
                cnt += 1

        if sum == K and cnt == N:
            ans += 1
    print(f'#{n+1}',ans)