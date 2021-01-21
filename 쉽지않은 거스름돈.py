T = int(input())
a = [50000,10000,5000,1000,500,100,50,10]
count = 0
for test_case in range(1,T+1):
    m = int(input());
    b = [0,0,0,0,0,0,0,0]
    for i in range(0,8):
        if m >= a[i]:
            for j in range(m//a[i]):
                m = m - a[i]
                b[i] = b[i] + 1
        else:
            continue
    print("#{}".format(test_case))
    print(f'{b[0]} {b[1]} {b[2]} {b[3]} {b[4]} {b[5]} {b[6]} {b[7]}')
