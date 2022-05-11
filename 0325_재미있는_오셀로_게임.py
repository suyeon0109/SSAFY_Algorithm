# 돌 탐색 방향
dx = [-1,-1,-1,0,1,1,1,0]
dy = [-1,0,1,1,1,0,-1,-1]

for tc in range(int(input())):
    N, M = map(int, input().split())
    oth = [[0]*N for _ in range(N)]
    a = (N-1)//2

		# 초기 돌 위치
    oth[a][a], oth[a][a+1], oth[a+1][a], oth[a+1][a+1] = 2,1,1,2
    
    for _ in range(M):
        col, row, stn = map(int, input().split())
        for i in range(8):
            k = 1
            change = []  # 돌을 뒤집을 위치를 넣을 리스트

						# 돌 탐색 위치가 판 내에 존재하고, 그 위치에 돌이 놓여져 있을 때. (돌이 없으면 탐색 x)
            while 0 <= row-1+dx[i]*k <= N-1 and 0 <= col-1+dy[i]*k <= N-1 and oth[row-1+dx[i]*k][col-1+dy[i]*k] != 0:
                r = row-1+dx[i]*k
                c = col-1+dy[i]*k

								# 해당 차례의 돌과, 이미 놓여져 있는 돌이 색이 다르면, 뒤집을 리스트에 위치 추가.
								# k에 1씩 더하면서 한칸 건너서 다시 탐색
                if oth[r][c] != stn:
                    k += 1
                    change.append((r,c))
                else:  # 색이 같은 돌을 만나면, 지금까지 change에 넣었던 위치의 돌들을 전부 뒤집는다.
                    for p,q in change:
                        oth[p][q] = stn
                    break

						# 뒤집을 돌을 전부 뒤집거나 혹은 아무일도 일어나지 않았을 경우 해당 차례 돌을 놓는다.
            oth[row-1][col-1] = stn

    cnt_1 = 0
    cnt_2 = 0

    for z in oth:
        cnt_1 += z.count(1)
        cnt_2 += z.count(2)
    
    print(f'#{tc+1}', cnt_1, cnt_2)