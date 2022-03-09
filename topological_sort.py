# 2050. Parallel Courses III


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        inDegree = [0] * n
        for prv, nxt in relations:
            prv, nxt = prv - 1, nxt - 1  # convert into zero-based index
            graph[prv].append(nxt)
            inDegree[nxt] += 1

        q = deque([])
        dist = [0] * n
        for u in range(n):
            if inDegree[u] == 0:
                q.append(u)
                dist[u] = time[u]

        while q:
            u = q.popleft()
            for v in graph[u]:
                dist[v] = max(
                    dist[u] + time[v], dist[v]
                )  # Update `dist[v]` using the maximum dist of the predecessor nodes
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)
        return max(dist)
