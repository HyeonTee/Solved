N = int(input())

if N < 10:
    print(N)

else:
    cnt = 9
    for i in range(10,N+1):
        i_str = str(i)
        d = int(i_str[1]) - int(i_str[0])
        
        ok = 1

        for t in range(len(i_str)-1):
            dt = int(i_str[t+1]) - int(i_str[t])
            if d != dt:
                ok = 0

        cnt += ok

    print(cnt)