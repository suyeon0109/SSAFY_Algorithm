from copy import deepcopy

for tc in range(int(input())):
    N = int(input())
    g1,p1 = map(int, input().split())
    gate1 = [g1-1,p1]
    z1 = p1
    g2,p2 = map(int, input().split())
    gate2 = [g2-1,p2]
    z2 = p2
    g3,p3 = map(int, input().split())
    gate3 = [g3-1,p3]
    z3 = p3
    copy_fish = [0]*N

    order = [[gate1,gate2,gate3],[gate1,gate3,gate2],[gate2,gate1,gate3],[gate2,gate3,gate1],[gate3,gate2,gate1],[gate3,gate1,gate2]]
    # [[gate1,gate2,gate3],[gate1,gate3,gate2],[gate2,gate1,gate3],[gate2,gate3,gate1],[gate3,gate2,gate1],[gate3,gate1,gate2]]
    s_min = N*(N+1)//2

    for i in order:
        fish = deepcopy(copy_fish)
        gate1[1] = z1
        gate2[1] = z2
        gate3[1] = z3
        s = 0
        for _ in range(2):
            fish1 = deepcopy(fish)
            gate1[1] = z1
            gate2[1] = z2
            gate3[1] = z3
            t = 0
            k = 1
            while i[0][1]:
                if 0 <= i[0][0]-t*k <= N-1:
                    if fish1[i[0][0]-t*k] == 0:
                        fish1[i[0][0]-t*k] = 1
                        i[0][1] -= 1
                        s += abs(t*k)+1
                k = k*(-1)
                if k == -1:
                    t += 1
            s1 = s
            for _ in range(2):
                gate1[1] = z1
                gate2[1] = z2
                gate3[1] = z3
                fish2 = deepcopy(fish1)
                s = s1
                t = 0
                k = 1
                while i[1][1]:
                    if 0 <= i[1][0]-t*k <= N-1:
                        if fish2[i[1][0]-t*k] == 0:
                            fish2[i[1][0]-t*k] = 1
                            i[1][1] -= 1
                            s += abs(t*k)+1
                    k = k*(-1)
                    if k == -1:
                        t += 1
                s2 = s

                for _ in range(2):
                    gate1[1] = z1
                    gate2[1] = z2
                    gate3[1] = z3
                    fish3 = deepcopy(fish2)
                    s = s2
                    t = 0
                    k = 1
                    while i[2][1]:
                        if 0 <= i[2][0]-t*k <= N-1:
                            if fish3[i[2][0]-t*k] == 0:
                                fish3[i[2][0]-t*k] = 1
                                i[2][1] -= 1
                                s += abs(t*k)+1
                        k = k*(-1)
                        if k == -1:
                            t += 1
                    if s < s_min:
                        s_min = s

    print(f'#{tc+1}',s_min)