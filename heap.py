class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [(-v, k) for k, v in Counter(s).items()]
        heapq.heapify(heap)
        prev, res = None, ''

        while heap:
            v, k = heapq.heappop(heap)
            res += k
            if prev: heapq.heappush(heap, prev)
            prev = (v + 1, k) if v+ 1 < 0 else None
        return '' if prev else res
