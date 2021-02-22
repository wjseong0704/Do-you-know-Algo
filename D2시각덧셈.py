T = int(input())
for test_case in range(1,T+1):
    H1,M1,H2,M2 = list(map(int, input().split(" ")))
    if (H1 + H2 + ((M1+M2)//60))%12 == 0:
        H = (H1 + H2 + ((M1+M2)//60))%12 + 12
    else:
        H = (H1 + H2 + ((M1+M2)//60))%12
    M = (M1 + M2)%60
    print(f'#{test_case} {H} {M}')
