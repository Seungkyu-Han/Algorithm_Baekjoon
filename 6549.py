import sys

while True:

    histo = list(map(int, sys.stdin.readline().split()))

    if histo[0] == 0:
        break

    res = 0

    def solve(left, right):

        if left > right:
            return 0

        if left == right:
            return histo[left]

        mid = (left + right) // 2
        height = histo[mid]
        mid_area = height

        start, end = mid, mid

        for i in range(right - left):

            if start == left:
                end += 1
                height = min(height, histo[end])
                mid_area = max(mid_area, height * (end - start + 1))
                continue

            if end == right:
                start -= 1
                height = min(height, histo[start])
                mid_area = max(mid_area, height * (end - start + 1))
                continue

            if histo[start - 1] > histo[end + 1]:
                start -= 1
                height = min(height, histo[start])
                mid_area = max(mid_area, height * (end - start + 1))
                continue
            else:
                end += 1
                height = min(height, histo[end])
                mid_area = max(mid_area, height * (end - start + 1))
                continue

        return max(solve(left, mid - 1), mid_area, solve(mid + 1, right))

    print(solve(1, histo[0]))
