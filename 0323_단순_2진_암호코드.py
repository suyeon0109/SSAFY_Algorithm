from collections import deque
code_l = [[0,0,0,1,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],[0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]

for tc in range(int(input())):
    N, M = map(int, input().split())
    for _ in range(N):
        line = list(map(int, input()))
        if 1 in line:
            code = line
    
    for i in range(M-1, -1, -1):
        if code[i] == 1:
            break

    psw = deque()
    for j in range(i,i-55,-7):
        for k in range(10):
            if code_l[k] == code[j-6:j+1]:
                psw.appendleft(k)
                break
    a = psw[0]+psw[2]+psw[4]+psw[6]
    b = psw[1]+psw[3]+psw[5]
    c = psw[7]

    if (a*3 + b + c)%10 == 0:
        print(f'#{tc+1}',a+b+c)
    else:
        print(f'#{tc+1}',0)