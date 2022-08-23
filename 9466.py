import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    student = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [True] * (n + 1)
    result = n

    for i in range(1, n + 1):
        if visited[i]:
            tmp = []
            cur = i

            while visited[cur]:
                tmp.append(cur)
                visited[cur] = False
                cur = student[cur]

            tmp_len = len(tmp)
            tmp.append(student[tmp[-1]])
            target = student[tmp[-2]]
            target_index = tmp.index(target)

            if target_index != tmp_len:
                result -= tmp_len - target_index
    print(result)
