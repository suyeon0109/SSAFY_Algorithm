for j in range(int(input())):
    n = int(input())
    la = list(map(int, input().split()))

    for _ in range(len(la)-1):
        for i in range(len(la)-1):
            if la[i]>la[i+1]:
                la[i], la[i+1] = la[i+1], la[i]

    print(f'#{j+1}', end=' ')
    for k in range(5):
        print(la[(k+1)*(-1)],la[k], end=' ')
    print()
