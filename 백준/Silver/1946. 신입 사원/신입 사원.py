import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    applicants = [0] * N
    hired = 0

    for i in range(N):
        first, second = map(int, input().split())
        applicants[i] = (first, second)
    
    applicants.sort()
    second_min = N+1

    for applicant in applicants:
        if applicant[1] < second_min:
            second_min = applicant[1]
            hired += 1
    
    print(hired)