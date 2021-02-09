T = int(input())
for test_case in range(1,T+1):
    a = list(map(str, input()))
    flag = True
    for i in range(1, len(a)):
        if a[i-1] != a[len(a)-i]:
            flag = False
    if flag :
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")
