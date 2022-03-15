for tc in range(int(input())):
    m = input()
    stk = ['!']
    calc = {'+':1, '*':2, '!':0}
    n = ''

    for i in range(len(m)):
        if 47 < ord(m[i]) < 58:
            n += m[i]
        else:
            while calc[stk[-1]] >= calc[m[i]]:
                n += stk.pop()
            stk.append(m[i])

    while stk:
        n+=stk.pop()

    print(f'#{tc+1}',n[:-1])