for tc in range(int(input())):
    n = float(input())
    cnt = 0
    m = ''
    while cnt < 13:
        if n*2 > 1:
            m += '1'
            if n*2 - 1 == n:
                print(f'#{tc+1}',m)
                break
            else:
                n = n*2 - 1
        elif n*2 == 1:
            m += '1'
            print(f'#{tc+1}',m)
            break
        else:
            m += '0'
            n *= 2
        cnt += 1
    else:
        print(f'#{tc+1}','overflow')

