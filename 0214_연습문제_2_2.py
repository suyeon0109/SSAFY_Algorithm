for _ in range(int(input())):
    la = list(map(int, input().split()))
    sum = 0
    for i in range(2 ** 10):
        for j in range(10):
            if i & (j<<10):
                sum += la[j]