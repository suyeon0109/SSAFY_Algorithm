for tc in range(int(input())):
    N, B = map(int, input().split())
    hum = list(map(int, input().split()))
    min_sum = 1000000

    for i in range(2 ** N):
        sum_hum = 0
        for j in range(N):
            if i & (1<<j):
                sum_hum += hum[j]

        if sum_hum >= B:
            if min_sum > sum_hum - B:
                min_sum = sum_hum - B
    print(f'#{tc+1}', min_sum)