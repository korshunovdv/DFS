def dfs(graph, visited, entrypoint, color):
    stack = []
    stack.append(entrypoint)
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = color
            for next_vertex in graph[vertex]:
                if not visited[next_vertex]:
                    stack.append(next_vertex)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        vertices, edges = map(int, file.readline().split())
        graph = [[] for i in range(vertices)]

        for _ in range(edges):
            start, finish = map(int, file.readline().split())
            graph[start].append(finish)
            graph[finish].append(start)

    visited = [0] * vertices
    color = 0
    for vertex in range(vertices):
        if not visited[vertex]:
            color += 1
            dfs(graph, visited, vertex, color)

    storage = [[] for _ in range(color)]
    for vertex, clr in enumerate(visited):
        storage[clr - 1].append(vertex)

    print(color)
    for connected in storage:
        print(len(connected))
        print(' '.join(map(str, connected)))

