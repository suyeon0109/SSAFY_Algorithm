from itertools import combinations

for tc in range(int(input())):
    N = int(input())
    ingred = [i for i in range(N)]
    table = [list(map(int, input().split())) for _ in range(N)]
    ingred_A = list(combinations(ingred, N//2))
    mini = 20000*(N**2)

    table_sum = 0
    for i in table:
        table_sum += sum(i)
    
    for p in ingred_A:
        ingred_B = list(set(ingred) - set(p))
        A, B = 0,0
        for i in range(N//2):
            for j in range(i+1,N//2):
                A += table[p[i]][p[j]] + table[p[j]][p[i]]
                B += table[ingred_B[i]][ingred_B[j]] + table[ingred_B[j]][ingred_B[i]]

        if abs(A-B) < mini:
            mini = abs(A-B)

    print(f'#{tc+1}',mini)