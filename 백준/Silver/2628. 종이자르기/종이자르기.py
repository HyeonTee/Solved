width_end, height_end = map(int, input().split())
width = [0,width_end]
height = [0,height_end]

n = int(input())

for _ in range(n):
    dir, cut = map(int, input().split())
    if dir == 1:
        width.append(cut)
    else:
        height.append(cut)

width.sort()
height.sort()

width_max = 0
for i in range(len(width)-1):
    width_now = width[i+1] - width[i]
    if width_now > width_max:
        width_max = width_now

height_max = 0
for i in range(len(height)-1):
    height_now = height[i+1] - height[i]
    if height_now > height_max:
        height_max = height_now

print(height_max * width_max)