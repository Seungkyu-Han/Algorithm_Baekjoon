import sys

L, C = map(int, sys.stdin.readline().split())
words = sorted(list(sys.stdin.readline().split()))

vowels = ['a', 'e', 'i', 'o', 'u']


def backtracking(cur_words, cur_cnt, cur_index):
    if cur_cnt == L:
        v_count, c_count = 0, 0
        for i in cur_words:
            if i in vowels:
                v_count += 1
            else:
                c_count += 1
        if v_count > 0 and c_count > 1:
            print(''.join(cur_words))
        return

    for i in range(cur_index, C):
        backtracking(cur_words + [words[i]], cur_cnt + 1, i + 1)


backtracking([], 0, 0)
