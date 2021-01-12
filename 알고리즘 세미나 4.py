T = int(input())
for test_case in range(1, T + 1):
    array = list(map(int, input().split(" ")))
    i = max(array);
    print("#{} {}".format(test_case, i))
