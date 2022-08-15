import sys

words = []

while True:
    tmp = sys.stdin.readline().strip()
    if tmp == "-":
        break
    words.append(tmp)

while True:

    puzzle = sys.stdin.readline().strip()
    if puzzle == "#":
        break

    al = [0] * 26

    for word in words:
        tmp_al = [0] * 26
        flag = True
        for t in range(9):
            tmp_al[ord(puzzle[t])-65] += 1

        for t in word:
            tmp_al[ord(t) - 65] -= 1
            if tmp_al[ord(t) - 65] < 0:
                flag = False
        if flag:
            for t in set(word):
                al[ord(t) - 65] += 1
    puzzle_set = list(set(puzzle))
    result = []
    for i in puzzle_set:
        result.append(al[ord(i) - 65])

    min_result = min(result)
    max_result = max(result)
    min_output = []
    max_output = []
    for i in range(len(result)):
        if max_result == result[i]:
            max_output.append(puzzle_set[i])

        if min_result == result[i]:
            min_output.append(puzzle_set[i])
    min_output.sort()
    max_output.sort()
    min_output = ''.join(min_output)
    max_output = ''.join(max_output)

    print(min_output, min_result, max_output, max_result)
