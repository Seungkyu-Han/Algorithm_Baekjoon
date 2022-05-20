import sys


class MST:

    def __init__(self, init_graph):
        self.graph = init_graph

    parent = dict()
    rank = dict()

    def make_set(self, node):
        self.parent[node] = node
        self.rank[node] = node

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1

    def kruskal(self):
        mst = []

        # 1. 초기화
        for i in self.graph[0]:
            self.make_set(i)

        # 2. 간선 기반 정렬
        edges = self.graph[1]
        edges.sort(key=lambda x: x[2])

        # 3. 붙이기
        for edge in edges:
            vertice_a, vertice_b, weight = edge
            if self.find(vertice_a) != self.find(vertice_b):
                self.union(vertice_a, vertice_b)
                mst.append(edge)
        return mst

    def find_result(self):
        mst = self.kruskal()
        total = 0
        for i in mst:
            total += i[2]
        return total


V, E = map(int, sys.stdin.readline().split())

graph = [[i for i in range(V + 1)], []]

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[1].append((a, b, c))


MyMst = MST(graph)
print(MyMst.find_result())
