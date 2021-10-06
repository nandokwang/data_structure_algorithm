# 시험을 준비하는 여러분은 방법 2 를 정확히 이해하고 구현할 수 있을 때까지 연습해야 한다. 특히 알고리즘 대회를 준비하는 독자라면 다익스트라 최단 경로 알고리즘은 자다가도 일어나서 바로 코드를 작성할 수 있을 정도로 코드에 숙달되어 있어야 한다. 또한 최단 경로 알고리즘을 응용해서 풀수 있는 고난이도 문제들이 많으므로 방법 2 를 이해하고 정확히 구현할 수 있다면 다양한 고난이도문제를 만났을 때에도 도움을 얻을 수 있다.

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = 6, 11
# 시작 노드 번호를 입력받기
start = 1
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

data = [
    '1 2 3', '1 3 5', '1 4 1', '2 3 3', 
    '2 4 2', '3 2 3', '3 6 5', '4 3 3', 
    '4 5 1', '5 3 1', '5 6 2']

# 모든 간선 정보를 입력받기
for d in data:
    a, b, c = map(int, d.split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

