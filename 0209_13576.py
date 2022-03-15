for i in range(int(input())):
    n = int(input())
    la = list(map(int, input().split()))
    drop = 0
    for j in range(len(la)):
        cnt = 0
        if j == 0:
            for k in range(j + 1, len(la)):
                if la[k] >= la[j]:
                        cnt += 1
        elif j >= 1:
            if la[j-1] < la[j]:
                for k in range(j+1, len(la)):
                    if la[k] >= la[j]:
                        cnt += 1
            else:
                continue


        if n - cnt - j - 1 > drop:
            drop = n - cnt - j - 1
        

    print(f'#{i+1}', drop)

