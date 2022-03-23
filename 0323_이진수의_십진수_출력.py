for tc in range(int(input())):
    la = list(map(int, input()))
    lb = []

    num = 0
    for i in range(6,len(la),7):
        for j in range(i,i-7,-1):
            num += la[j]*(2**(6 - j%7))
        lb.append(num)
        num = 0
    
    print(f'#{tc+1}',*lb)