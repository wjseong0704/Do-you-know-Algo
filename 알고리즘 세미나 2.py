import sys

T = int(input())
for test_case in range(1, T + 1):
    array = list(map(int, input().split(" ")))
    i = 0;
    sum = 0;
    for i in range(len(array)):
            sum += array[i]
        
    avr = round(sum/len(array))
    
    
    print("#{} {}".format(test_case, avr))
