for tc in range(int(input())):
    m = ''
    for i in input()[::-1]:
        if i ==  'p' :
            m += 'q'
        elif i == 'q':
            m += 'p'
        elif i == 'b':
            m += 'd'
        else:
            m += 'b'
    
    print(f'#{tc+1}',m)