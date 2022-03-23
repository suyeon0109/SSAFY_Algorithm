for tc in range(int(input())):
    la = list(map(str, input().split()))
    stk = []
    for i in la:
        try:
            if i == '+':
                stk.append(stk.pop() + stk.pop())
            elif i == '-':
                stk.append(stk.pop(-2) - stk.pop())
            elif i == '*':
                stk.append(stk.pop() * stk.pop())
            elif i == '/':
                stk.append(stk.pop(-2) // stk.pop())
            elif i == '.':
                result = stk.pop()
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