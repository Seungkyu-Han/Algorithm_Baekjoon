import sys

R, C = map(int, sys.stdin.readline().split())

board = []

for i in range(R):
    board.append(list(sys.stdin.readline().strip()))

result = 0


def move(cur_x, cur_y, cnt, visited):
    global result
    result = max(result, cnt)

    for go_x, go_y in [(cur_x - 1, cur_y), (cur_x + 1, cur_y), (cur_x, cur_y - 1), (cur_x, cur_y + 1)]:
        if 0 <= go_x < R and 0 <= go_y < C:
            target = ord(board[go_x][go_y]) - 65
            if visited[target]:
                visited[target] = False
                move(go_x, go_y, cnt + 1, visited)
                visited[target] = True

    return


input_visited = [True for i in range(ord('Z') - ord('A') + 1)]
input_visited[ord(board[0][0]) - 65] = False
move(0, 0, 1, input_visited)
print(result)
