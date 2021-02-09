T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    if(N%2 == 1):
        print(f"#{test_case} {(N+1)//2}")
    else:
        print(f"#{test_case} -{N//2}")
