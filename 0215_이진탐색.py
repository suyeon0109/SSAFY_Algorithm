for i in range(int(input())):
    p_init, A, B = map(int, input().split())
    la = [A, B]

    for j in range(2):

        s = 1
        f = p_init
        cnt = 0
        p = s+f

        while la[j] != p:
            cnt += 1
            p = (s+f)//2
            if p < la[j]:
                s = p
            elif la[j] < p:
                f = p
            else:
                break
        la[j] = cnt

    if la[0]<la[1]:
        print(f'#{i+1} A')
    elif la[0]>la[1]:
        print(f'#{i+1} B')
    else:
        print(f'#{i+1} 0')