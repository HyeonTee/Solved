C = int(input())

for _ in range(C):
    scores = list(map(int, input().split()))
    N = scores[0]
    del scores[0]
    
    scoreSum = 0
    for i in scores:
        scoreSum += i
    scoreMean = scoreSum / N
    
    passNum = 0
    for i in scores:
        if i > scoreMean:
            passNum += 1
    
    passRate = passNum / N * 100
    print("%.3f%%" %passRate)