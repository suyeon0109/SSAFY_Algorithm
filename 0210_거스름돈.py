for j in range(int(input())):
    n = int(input())
    la = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    lb = [0]*8
    for i in range(len(la)):
        lb[i] = n//la[i]
        n %=la[i]
    
    print(f'#{j+1}')
    print(*lb)