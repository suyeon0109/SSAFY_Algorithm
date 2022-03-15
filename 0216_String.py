for tc in range(10):
    n = int(input())
    tg = input()
    ch = input()

    cnt = 0
    for i in range(len(ch)):
        if ch[i:i+len(tg)] == tg:
            cnt += 1
    
    print(f'#{tc+1}', cnt)
