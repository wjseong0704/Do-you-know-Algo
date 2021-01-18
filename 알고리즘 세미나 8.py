A = list(map(str,input()))
B = []
for i in range(len(A)):
    B.append(ord(A[i]))
    print(B[i]-64,end = ' ')
