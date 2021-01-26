from collections import deque

def solution(st, t):
    dq = deque([])
    dq1 = deque([])
    for i in st:
        if i == "#" and dq:
            dq.pop()
        elif i!="#":
            dq.append(i)
    
    for j in t:
        if j == "#" and dq1:
            dq1.pop()
        elif j!="#":
            dq1.append(j)
    
    print(dq,dq1)
    print(dq==dq1)

solution('a##c','#a#c')

