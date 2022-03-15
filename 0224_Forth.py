for tc in range(int(input())):
    la = list(map(str, input().split()))
    stk = []
    for i in la:
        try:
            if i == '+':
                stk.append(stk.pop(-1) + stk.pop(-1))
            elif i == '-':
                stk.append(stk.pop(-1) - stk.pop(-1))
            elif i == '*':
                stk.append(stk.pop(-1) * stk.pop(-1))
            elif i == '/':
                stk.append(stk.pop(-1) // stk.pop(-1))
            elif i == '.':
                if la.index(i) == len(la)-1:
                    result = stk.pop(-1)
                else:
                    print(f'#{tc+1} error')
                    break
            else:
                stk.append(int(i))
        except:
            print(f'#{tc+1} error')
            break
    else:
        if stk:
            print(f'#{tc+1} error')
        else:
            print(f'#{tc+1}', result)