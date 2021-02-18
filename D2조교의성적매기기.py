T = int(input())
for test_case in range(1,T+1):
    N, K = list(map(int, input().split(" ")))
    student = []
    final = []
    for i in range(N):
        score = list(map(int, input().split(" ")))
        student.append(score)
    #print(student)
    for i in range(N):
        j = (0.35*student[i][0] + 0.45*student[i][1] + 0.2*student[i][2])
        final.append(j)
        if i+1 == K:
            w = final[i]
    #print(final)
    #print(w)
    final.sort(reverse=True)
    #print(final)
    grade = ['A+', 'A0', 'A-', 'B+', 'B0','B-', 'C+', 'C0', 'C-', 'D0']
    #print(grade)
    for i in range(0,N):
        if w == final[i]:
            print(f'#{test_case} {grade[i//(N//10)]}')
        #final[i] = grade[i//(N//10)]
    #print(final)
 
