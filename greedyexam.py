T = int(input())
for test_case in range(1, T + 1):
    N, K = list(map(int, input().strip( ).split(" ")))
    A = 0
    while(N >= K):
        A += N%K +1
        N = N//K
    print(f'#{test_case} {A+N-1}')
