for tc in range(int(input())):
    la = [input() for _ in range(5)]

    length = 0
    for i in la:
        if len(i)>length:
            length = len(i)

    for p in range(len(la)):
        if len(la[p]) < length:
            la[p] += (length-len(la[p])) * '_'

    m = ''
    for k in range(length):
        for j in la:
            if j[k] == '_':
                pass
            else:
                m += j[k]
    
    print(f'#{tc+1}',m)