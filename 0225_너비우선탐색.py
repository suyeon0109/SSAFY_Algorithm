def enq(n):
        global rear 
        if isFull():
            print('Q is Full')
        else:
            rear += 1
            Q[rear] = n
def deq():
    if isEmp():
        return 'Q is empty'
    else:
        global front
        front += 1
        return Q[front]
def isEmp():
    return front == rear
def isFull():
    return rear == len(Q)-1
def Qpeek():
    return Q[front+1]

for tc in range(int(input())):
    V, E = map(int, input().split())
    adj = [[0]*(V + 1) for _ in range(V + 1)]
    visited = []
    Q = [0]*V

    front = rear = -1

    for _ in range(E):
        a,b = map(int, input().split())
        adj[a][b], adj[b][a] = 1, 1
    
    enq(1)
    while not isEmp():
        t = deq()
        visited.append(t)
        for i in range(V+1):
            if adj[t][i] == 1:
                if i not in Q:
                    enq(i)
    
    print(f'#{tc+1}',*visited)
    
