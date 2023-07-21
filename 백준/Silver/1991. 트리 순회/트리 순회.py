tree = {}

n = int(input())

for i in range(n):
    k, lt, rt = input().split()
    tree[k] = (lt, rt)

def preorder(key):
    print(key, end = '')
    if tree[key][0] != '.':
        preorder(tree[key][0])
    if tree[key][1] != '.':
        preorder(tree[key][1])

def inorder(key):
    if tree[key][0] != '.':
        inorder(tree[key][0])
    print(key, end = '')
    if tree[key][1] != '.':
        inorder(tree[key][1])

def postorder(key):
    if tree[key][0] != '.':
        postorder(tree[key][0])
    if tree[key][1] != '.':
        postorder(tree[key][1])
    print(key, end = '')
        

preorder('A')
print()
inorder('A')
print()
postorder('A')