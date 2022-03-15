for i in range(int(input())):
    n = int(input())
    number = input()

    la = [0]*10
    for j in number:
        la[int(j)] += 1
    
    max = 0
    for k in range(len(la)):
        if la[k] >= max:
            max = la[k]
            idx = k
    
    print(f'#{i+1}',idx, max)
