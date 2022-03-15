for tc in range(int(input())):
    m = input()
    la = [0]
    for i in m:
        if i == '(' or i == '{':
            la.append(i)
        elif i == ')':
            if la[-1] == '(':
                la.pop()
            else:
                break
        elif i == '}':
            if la[-1] == '{':
                la.pop()
            else:
                break
    
    if len(la) == 0:
        print(f'#{tc+1}',1)
    else:
        print(f'#{tc+1}',0)