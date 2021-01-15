T = int(input())
for test_case in range(1, T + 1):
    array = []
    for i in input():
        array.append(i)
    yyyy = "".join(map(str, array[:4]))
    mm = "".join(map(str, array[4:6]))
    dd = "".join(map(str, array[6:]))
    if int(mm) == 2 and int(dd) > 28:
        print("#{} -1".format(test_case))
    elif int(mm)%2 == 1 and int(dd)>31:
        print("#{} -1".format(test_case))
    elif int(mm)%2 == 0 and int(dd)>30:
        print("#{} -1".format(test_case))
    elif int(mm)>12:
        print("#{} -1".format(test_case))
    elif int(mm) == 0:
        print("#{} -1".format(test_case))
    else:
        print("#{} {}/{}/{}".format(test_case,yyyy,mm,dd))
