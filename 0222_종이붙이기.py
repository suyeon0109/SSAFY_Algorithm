def paper(N):
    la = [1,3]
    for i in range(2, N//10):
        la.append(la[i-2]*2 + la[i-1])
    
    return la[N//10-1]

for tc in range(int(input())):
    N = int(input())
    print(paper(N))
