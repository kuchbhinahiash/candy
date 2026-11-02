"""
GD 9 - Graph of popular locations in an area.
  BFS uses an ADJACENCY LIST  (with a queue)
  DFS uses an ADJACENCY MATRIX (with a stack / recursion)
Undirected graph: an edge means a route exists between two locations.
"""

from collections import deque


class Graph:
    def __init__(self, locations):
        self.locations = locations                       # e.g. ['A','B','C']
        self.n = len(locations)
        self.index = {loc: i for i, loc in enumerate(locations)}
        self.matrix = [[0] * self.n for _ in range(self.n)]   # adjacency matrix
        self.adj = {loc: [] for loc in locations}             # adjacency list

    def add_route(self, u, v):
        i, j = self.index[u], self.index[v]
        self.matrix[i][j] = self.matrix[j][i] = 1
        if v not in self.adj[u]:
            self.adj[u].append(v)
        if u not in self.adj[v]:
            self.adj[v].append(u)

    # ---- BFS using adjacency list + queue ----
    def bfs(self, start):
        visited = {start}
        queue = deque([start])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for nb in self.adj[node]:
                if nb not in visited:
                    visited.add(nb)
                    queue.append(nb)
        return order

    # ---- DFS using adjacency matrix (recursive) ----
    def dfs(self, start):
        visited = [False] * self.n
        order = []

        def visit(i):
            visited[i] = True
            order.append(self.locations[i])
            for j in range(self.n):
                if self.matrix[i][j] == 1 and not visited[j]:
                    visit(j)

        visit(self.index[start])
        return order

    def show(self):
        print("\nAdjacency Matrix:")
        print("   " + "  ".join(self.locations))
        for i, row in enumerate(self.matrix):
            print(f"{self.locations[i]}  " + "  ".join(map(str, row)))
        print("\nAdjacency List:")
        for loc in self.locations:
            print(f"{loc} -> {self.adj[loc]}")


def main():
    print("=== Locations Graph: BFS & DFS ===")
    if input("Use sample graph? (y/n): ").lower() == "n":
        locs = input("Enter locations separated by space (e.g. A B C D): ").split()
        g = Graph(locs)
        e = int(input("Number of routes: "))
        for _ in range(e):
            u, v = input("Route between (e.g. A B): ").split()
            g.add_route(u, v)
    else:
        g = Graph(["A", "B", "C", "D", "E", "F"])
        for u, v in [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("D", "F"), ("E", "F")]:
            g.add_route(u, v)

    g.show()
    start = input("\nStart location (e.g. A): ").strip() or g.locations[0]
    print("\nBFS (adjacency list)  :", " -> ".join(g.bfs(start)))
    print("DFS (adjacency matrix):", " -> ".join(g.dfs(start)))
    print("\nComplexity:")
    print("  BFS (adj list)  : Time O(V + E)   Space O(V)")
    print("  DFS (adj matrix): Time O(V^2)     Space O(V^2) for matrix + O(V) recursion")


if __name__ == "__main__":
    main()
