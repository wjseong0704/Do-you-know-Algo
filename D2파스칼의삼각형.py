def pascal(list a):
    i = 0
    for i in range(1,len(a)):
        b[i] = a[i-1] + a[i]

T = int(input())
for test_case in range(1,T+1):
    w = int(input())
    a = [1,1,1]
    for i in range(w):
