'''
def left(i,j):
    i = i
    j = j-1
    return i,j
def right(i,j):
    i = i
    j = j+1
    return i,j
def up(i,j):
    i = i-1
    j = j
    return i,j
def down(i,j):
    i = i+1
    j = j
    return i,j

#T = int(input())
#for test_case in range(1,T+1):
#사각형만들기
N = int(input())
square = [[0] * N for s in range(N)]
#inner = [0] * N
#for i in range(N):
#    inner.append(i)
#    square.append(inner)
print(square)
#초기값 설정
if N%2 == 0:
    a = N//2
    b = N//2 -1
    square[a][b] = N*N
else:
    a = N//2
    b = N//2
    square[a][b] = N*N
    flag = True
print(square)
#길 뚫기
#test = [[1,2,3],[4,5,6],[7,8,9]]
w = []
for i in range(N*N):
    w.append(i)
w.reverse()
print(w)

for i in range(N):
    if a == 0 or b == 0:
        flag = False
   
for i in range(1,N):
    if flag:
        a = a 
        b = b + (-1)*flag
        print(a,b)
    else:
        a = a
'''
#사각형만들기
N = int(input())
square = [[0] * N for s in range(N)]
print(square)

#초기값 설정
w = []
for i in range(N*N):
    w.append(N*N-i)
#w.reverse()
print(w)

if N%2 == 0:
    a = N//2
    b = N//2 -1
    square[a][b] = w[0]
else:
    a = N//2
    b = N//2
    square[a][b] = w[0]
print(square)

#길 뚫기

j = True
k = False

for i in range(1,N):
    print(i)
    (a, b) = (a, b+(-1)**j*i)
    (a, b) = (a+(-1)**k*i, b)
    if 
