#T = int(input())
#for test_case in range(1,T+1):
N = int(input())
student = []
for i in range(N):
    score = list(map(int, input().split(" ")))
    student.append(score)
print(student)
