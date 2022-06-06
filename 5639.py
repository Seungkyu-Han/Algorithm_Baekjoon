import sys

sys.setrecursionlimit(10**6)


class Tree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.head = None

    def make_head(self, data):
        self.head = self.Node(data)

    def insert(self, data):
        cur = self.head
        while True:
            if data < cur.data:
                if cur.left is None:
                    cur.left = self.Node(data)
                    return
                else:
                    cur = cur.left
            else:
                if cur.right is None:
                    cur.right = self.Node(data)
                    return
                else:
                    cur = cur.right
    result = []

    def to_inorder(self, target):
        if target.left is not None:
            self.to_inorder(target.left)
        if target.right is not None:
            self.to_inorder(target.right)
        self.result.append(target.data)
        return

    def inorder(self):
        self.result.clear()
        cur = self.head
        self.to_inorder(cur)
        return self.result


input_data = []

while True:
    try:
        input_data.append(int(sys.stdin.readline()))
    except:
        break

myTree = Tree()
myTree.make_head(input_data[0])

for i in input_data[1:]:
    myTree.insert(i)

myresult = myTree.inorder()

for i in myresult:
    print(i)
