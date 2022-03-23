parent = [0] * 14
la = list(map(int, input().split()))

for i in range(0,len(la),2):
    parent[la[i+1]] = la[i]

while 1:
    a = parent.index(max(parent))