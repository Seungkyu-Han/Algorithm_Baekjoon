import sys


class Heap:
    def __init__(self):
        self.heap_array = [None]
        self.size = 0

    def move_up(self, index):
        if self.size <= 1:
            return False
        if self.heap_array[index // 2] is not None and self.heap_array[index] > self.heap_array[index // 2]:
            return True
        else:
            return False

    def move_down(self, index):
        if self.size < 2:
            return 0
        desc1_index = index * 2
        desc2_index = index * 2 + 1
        if desc1_index > self.size:
            return 0
        if desc2_index > self.size:
            if self.heap_array[desc1_index] > self.heap_array[index]:
                return 1
            else:
                return 0
        if self.heap_array[desc1_index] > self.heap_array[desc2_index]:
            if self.heap_array[desc1_index] > self.heap_array[index]:
                return 1
            else:
                return 0
        else:
            if self.heap_array[desc2_index] > self.heap_array[index]:
                return 2
            else:
                return 0

    def insert(self, data):
        self.size += 1
        self.heap_array.append(data)
        index = self.size
        while self.move_up(index):
            parent_index = index // 2
            self.heap_array[parent_index], self.heap_array[index] = self.heap_array[index], self.heap_array[parent_index]
            index = parent_index
        return True

    def pop(self):
        if self.size < 1:
            return 0
        result = self.heap_array[1]
        self.heap_array[1] = self.heap_array[self.size]
        del self.heap_array[-1]
        cur_index = 1
        self.size -= 1
        flag = self.move_down(cur_index)
        while flag > 0:
            if flag == 1:
                self.heap_array[cur_index], self.heap_array[cur_index * 2] =\
                    self.heap_array[cur_index * 2], self.heap_array[cur_index]
                cur_index = cur_index * 2
                flag = self.move_down(cur_index)
            else:
                self.heap_array[cur_index], self.heap_array[cur_index * 2 + 1] = \
                    self.heap_array[cur_index * 2 + 1], self.heap_array[cur_index]
                cur_index = cur_index * 2 + 1
                flag = self.move_down(cur_index)

        return result


num = int(sys.stdin.readline())
myheap = Heap()
for i in range(num):
    ans = int(sys.stdin.readline())
    if ans == 0:
        print(myheap.pop())
    else:
        myheap.insert(ans)
