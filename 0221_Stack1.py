for tc in range(int(input())):
    m = input()
    cnt_1 = 0
    cnt_2 = 0
    for i in m:
        if i == '(':
            cnt_1 += 1
        else:
            cnt_2 += 1
    
    if cnt_1 == cnt_2:
        if m[0] == ')' or m[-1] == '(':
            print(f'#{tc+1}', 0)
        else:
            print(f'#{tc+1}', 1)
    else:
        print(f'#{tc+1}', 0)