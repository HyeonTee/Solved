import sys

sys.setrecursionlimit(10**9)
input_list = []

while True:
    try:
        input_list.append(int(sys.stdin.readline()))
    except:
        break

def pre_to_post(preordered):
    if not preordered:
        return []
    else:
        root = preordered[0]
        lt_subtree = []
        rt_subtree = []
        for val in preordered:
            if val == root:
                pass
            elif val < root:
                lt_subtree.append(val)
            else:
                rt_subtree.append(val)
            
        return pre_to_post(lt_subtree) + pre_to_post(rt_subtree) + [root]

for node in pre_to_post(input_list):
    print(node)