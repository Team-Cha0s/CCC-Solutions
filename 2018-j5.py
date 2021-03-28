import queue
q = queue.Queue()
graph = {}
visited = []
dist = {}
checked = []
shortest = []
N = int(input())

def bfs(node):
    q.put(node)
    while not q.empty():
        u = q.get()
        checked.append(u)
        for v in graph[u]:
            if dist[v] == 0:
                dist[v] = dist[u] + 1
                q.put(v)


for i in range(1, N+1):
    graph[str(i)] = []
    line = input().split()
    if line != ['0']:
        for j in range(1, len(line)):
            if str(i) in graph.keys():
                graph[str(i)].append(line[j])
            else:
                graph[str(i)] = [line[j]]
    else:
        shortest.append(i)

for i in range(1, N+1):
    dist[str(i)] = 0

bfs('1')
if len(checked) >= len(graph.keys()):
    print("Y")
else:
    print("N")

l = []

for i in shortest:
    l.append(dist[str(i)])


for j in sorted(l):
    if j != 0:
        print(j+1)
        break