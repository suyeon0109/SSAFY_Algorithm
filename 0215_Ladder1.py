for tc in range(10):
    n = int(input())
    la = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    for k in range(102):
        if la[-1][k] == 2:
            i = 99
            j = k
    
    while i != 0:
        if la[i][j-1] == 1:
            while la[i][j-1] == 1:
                j -= 1
        elif la[i][j+1] == 1:
            while la[i][j+1] == 1:
                j += 1
        i -= 1
    
    print(f'#{tc+1}',j-1)