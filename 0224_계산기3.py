def change(m):
    rank = {'+':1, '-':1, '*':2, '/':2, '!':-1, '(':0}
    stk=['!']
    m_2 = ''
    for i in m:
        if i.isdigit():
            m_2 += i
        else:
            if i == '(':
                stk.append(i)
            else:
                if i == ')':
                    while 1:
                        t = stk.pop()
                        if t == '(':
                            break
                        m_2 += t
                else:
                    while rank[stk[-1]] >= rank[i]:
                        m_2 += stk.pop()
                    stk.append(i)
    while stk:
        m_2 += stk.pop()
    return(m_2[:-1])

def calc(m_2):
    stk = []
    for i in m_2:
        if i.isdigit():
            stk.append(int(i))
        else:
            if i == '+':
                stk.append(stk.pop(-1) + stk.pop(-1))
            elif i == '-':
                stk.append(stk.pop(-1) - stk.pop(-1))
            elif i == '*':
                stk.append(stk.pop(-1) * stk.pop(-1))
            elif i == '/':
                stk.append(stk.pop(-1) // stk.pop(-1))
    return stk[0]

for tc in range(10):
    n = int(input())
    m = input()
    print(f'#{tc+1}',calc(change(m)))