for tc in range(int(input())):
    a = input()
    b = input()
    cnt = 0
    maxc = 0

    for i in a:
        cnt = 0
        for j in b:
            if i == j:
                cnt += 1

        if maxc < cnt:
            maxc = cnt
    
    print(f'#{tc+1}',maxc)