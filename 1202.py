import sys, heapq


class MyHeap:

    def __init__(self):
        self.heap_list = [0] * 700000
        self.cur_len = 0

    def add(self, value):
        self.cur_len += 1
        self.heap_list[self.cur_len] = value
        cur_index = self.cur_len
        while cur_index > 1 and self.go_up(cur_index):
            cur_index //= 2
        return

    def go_up(self, index):
        if self.heap_list[index // 2] < self.heap_list[index]:
            self.heap_list[index // 2], self.heap_list[index] = self.heap_list[index], self.heap_list[index // 2]
            return True
        else:
            return False

    def pop(self):
        if self.cur_len < 1:
            return False

        return_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.cur_len]
        self.cur_len -= 1
        cur_index = 1

        while True:

            if cur_index * 2 > self.cur_len:
                break
            elif cur_index * 2 == self.cur_len:
                if self.heap_list[cur_index * 2] > self.heap_list[cur_index]:
                    self.heap_list[cur_index * 2], self.heap_list[cur_index] = self.heap_list[cur_index], self.heap_list[cur_index * 2]
                break
            else:
                if self.heap_list[cur_index * 2 + 1] > self.heap_list[cur_index * 2]:
                    if self.heap_list[cur_index] > self.heap_list[cur_index * 2 + 1]:
                        break
                    else:
                        self.heap_list[cur_index * 2 + 1], self.heap_list[cur_index] = self.heap_list[cur_index], self.heap_list[cur_index * 2 + 1]
                        cur_index = cur_index * 2 + 1
                else:
                    if self.heap_list[cur_index] > self.heap_list[cur_index * 2]:
                        break
                    else:
                        self.heap_list[cur_index * 2], self.heap_list[cur_index] = self.heap_list[cur_index], self.heap_list[cur_index * 2]
                        cur_index = cur_index * 2
        return return_value

    def return_len(self):
        return self.cur_len

    def peek(self):
        return self.heap_list[1]


steal = []
result = 0

N, K = map(int, sys.stdin.readline().split())

for i in range(N):
    heapq.heappush(steal, tuple(map(int, sys.stdin.readline().split())))

for i in range(K):
    heapq.heappush(steal, (int(sys.stdin.readline()), 1e9))

can = MyHeap()

while steal:
    cur_weight, cur_value = heapq.heappop(steal)

    if cur_value != 1e9:
        can.add(cur_value)
    else:
        if can.return_len() > 0:
            result += can.pop()

print(result)
