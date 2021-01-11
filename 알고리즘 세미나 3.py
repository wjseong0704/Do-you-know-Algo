T = int(input())
for test_case in range(1, T + 1):
    array = list(map(int, input().split(" ")))
    i = array[0];
    j = array[1];
    if i > j:
        print("#{} {}".format(test_case, ">"))
    elif i == j:
        print("#{} {}".format(test_case, "="))
    else:
        print("#{} {}".format(test_case, "<"))
