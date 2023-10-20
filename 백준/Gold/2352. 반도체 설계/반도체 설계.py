from bisect import bisect_left

n = input()
dest = list(map(int, input().split()))
link = []
for d in dest:
    if not link or link[-1] < d:
        link.append(d)
    else:
        link[bisect_left(link, d)] = d
print(len(link))