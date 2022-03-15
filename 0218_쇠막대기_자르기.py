for tc in range(int(input())):
    m = '0' + input() + '0'
    cnt = 0
    sum = 0

    for i in range(1,len(m)-1):
        if m[i:i+2] == '()':
            sum += cnt
        elif m[i] == '(':
            cnt += 1
        elif m[i-1:i+1] == '()':
            pass
        else:
            cnt -=1
            sum +=1

    print(f'#{tc+1}',sum)