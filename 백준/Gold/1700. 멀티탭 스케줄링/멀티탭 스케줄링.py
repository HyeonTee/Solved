import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = list(map(int, input().split()))
plugs = []
cnt = 0

for idx, item in enumerate(items):
    if item in plugs:
        continue
    
    elif len(plugs) < N:
        plugs.append(item)
    
    else:
        del_idx = 0
        max_idx = 0
        for i, p in enumerate(plugs):
            if p not in items[idx+1:]:
                del_idx = i
                break
            else:
                if items[idx+1:].index(p) > max_idx:
                    del_idx = i
                    max_idx = items[idx+1:].index(p)
        
        del plugs[del_idx]
        plugs.append(item)
        cnt += 1

print(cnt)