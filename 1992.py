import sys


def quad_tree(video_list, x, y, n):
    target = video_list[x][y]
    for j in range(n):
        for k in range(n):
            if video_list[x + j][y + k] != target:
                return "(" + quad_tree(video_list, x, y, n // 2) + quad_tree(video_list, x, y + n // 2, n // 2) + quad_tree(video_list, x + n // 2, y , n // 2) + quad_tree(video_list, x + n // 2, y + n // 2, n // 2) + ")"
    return str(target)


num = int(sys.stdin.readline())
myvideo = []
for i in range(num):
    tmp_list = list(sys.stdin.readline().strip())
    myvideo.append(tmp_list)

print(quad_tree(myvideo,0, 0, num))
