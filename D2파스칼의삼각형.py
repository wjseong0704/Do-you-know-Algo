T = int(input())
for test_case in range(1,T+1):
    w = int(input())
    a = [[1]] 
    for i in range(1, w):
        b = []
        b.append(1)
        for j in range(i-1):
            b.append(0)
            b[j+1] = a[i-1][j] + a[i-1][j+1]
        b.append(1)
        a.append(b)
    print(f"#{test_case}")
    for i in a:
        for j in i:
            print(j, end=' ')
        print()
