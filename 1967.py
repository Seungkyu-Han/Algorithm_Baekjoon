from collections import deque
import sys

num = int(sys.stdin.readline())

if num > 1:
    graph = {i + 1: [] for i in range(num)}

    for i in range(num - 1):
        start, end, length = map(int, sys.stdin.readline().split())
        graph[start].append((end, length))
        graph[end].append((start, length))


    def rad(target):
        need_visit = deque()
        need_visit.append(target)
        visited = [-1] * (num + 1)
        visited[target] = 0
        result = [0, 0]  # len, node
        while need_visit:
            cur = need_visit.pop()
            cur_list = graph[cur]
            cur_length = visited[cur]
            for ver, weight in cur_list:
                if visited[ver] == -1:
                    visited[ver] = cur_length + weight
                    need_visit.append(ver)
                    if visited[ver] > result[0]:
                        result = [visited[ver], ver]
        return result


    far_node = rad(1)[1]
    print(rad(far_node)[0])

else:
    print(0)
