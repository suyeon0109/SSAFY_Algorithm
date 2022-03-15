Q = [0]*3
front = rear = 0
def enq(n):
    global rear 
    if isEmp():
        print('Q is Full')
    else:
        rear = (rear+1)%len(Q)
        Q[rear] = n
def deq():
    if isEmp():
        return 'Q is empty'
    else:
        global front
        front = (front+1)%len(Q)
        return Q[front]

def isEmp():
    return front == rear
def isFull():
    return front == rear+1
    # front == (rear+1)%len(Q)
def Qpeek():
    return Q[front+1]

enq(1)
enq(2)
enq(3)
print(deq())
print(deq())
print(deq())