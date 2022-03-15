for tc in range(10):
    N = int(input())
    pswd = list(map(int, input().split()))
    M = int(input())
    order = list(map(str, input().split()))
 
    for i in range(len(order)):
        if order[i] == 'D':
            for _ in range(1,int(order[i+2])+1):
                pswd.pop(int(order[i+1]))
        elif order[i] == 'I':
            for k in range(int(order[i+2]),0,-1):
                pswd.insert(int(order[i+1]),order[i+2+k])
        elif order[i] == 'A':
            for k in range(int(order[i+1])):
                pswd.insert(-1,order[i+2+k])
     
    print(f'#{tc+1}',*pswd[:10])