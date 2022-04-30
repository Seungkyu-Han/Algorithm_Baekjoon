import sys


class AbsHeap:

    def __init__(self):
        self.array = [None]
        self.size = 0

    def insert(self, data):
        if self.size == 0:
            self.size += 1
            self.array.append(data)
            return
        self.size += 1
        self.array.append(data)
        index = self.size
        while self.move_up(index):
            self.array[index], self.array[index//2] = self.array[index//2], self.array[index]
            index //= 2
        return True

    def move_up(self, index):
        if index < 2:
            return False
        if abs(self.array[index]) < abs(self.array[index//2]):
            return True
        elif abs(self.array[index]) == abs(self.array[index//2]):
            if self.array[index] < self.array[index//2]:
                return True
            else:
                return False
        else:
            return False

    def pop(self):
        if self.size == 0:
            return 0
        result = self.array[1]
        self.array[1] = self.array[self.size]
        del self.array[-1]
        self.size -= 1
        index = 1
        flag = self.move_down(index)
        while flag > 0:
            if flag == 1:
                self.array[index], self.array[index * 2] = self.array[index * 2], self.array[index]
                index *= 2
                flag = self.move_down(index)
            else:
                self.array[index], self.array[index * 2 + 1] = self.array[index * 2 + 1], self.array[index]
                index = index * 2 + 1
                flag = self.move_down(index)
        return result

    def move_down(self, index):
        if self.size < 2:
            return 0
        left = index * 2
        right = index * 2 + 1
        if left > self.size:
            return 0
        if right > self.size:
            if abs(self.array[left]) < abs(self.array[index]):
                return 1
            elif abs(self.array[left]) == abs(self.array[index]):
                if self.array[left] < self.array[index]:
                    return 1
                else:
                    return 0
            else:
                return 0
        if abs(self.array[left]) < abs(self.array[right]):
            if abs(self.array[left]) < abs(self.array[index]):
                return 1
            elif abs(self.array[left]) == abs(self.array[index]):
                if self.array[left] < self.array[index]:
                    return 1
                else:
                    return 0
            else:
                return 0
        elif abs(self.array[left]) == abs(self.array[right]):
            if self.array[left] < self.array[right]:
                if abs(self.array[left]) == abs(self.array[index]):
                    if self.array[left] < self.array[index]:
                        return 1
                    else:
                        return 0
                elif abs(self.array[left]) < abs(self.array[index]):
                    return 1
                else:
                    return 0
            else:
                if abs(self.array[right]) == abs(self.array[index]):
                    if self.array[right] < self.array[index]:
                        return 2
                    else:
                        return 0
                elif abs(self.array[right]) < abs(self.array[index]):
                    return 2
                else:
                    return 0
        else:
            if abs(self.array[right]) < abs(self.array[index]):
                return 2
            elif abs(self.array[right]) == abs(self.array[index]):
                if self.array[right] < self.array[index]:
                    return 2
                else:
                    return 0
            else:
                return 0


myheap = AbsHeap()

cnt = int(sys.stdin.readline())

for i in range(cnt):
    ans = int(sys.stdin.readline())
    if ans == 0:
        print(myheap.pop())
    else:
        myheap.insert(ans)
