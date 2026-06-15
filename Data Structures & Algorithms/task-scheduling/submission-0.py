class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-a for a in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        while maxHeap or q:
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1
                if task != 0:
                    q.append([task, time + n])
            if q and time == q[0][1]:
                prev = q.popleft()
                heapq.heappush(maxHeap, prev[0])
            time += 1
            print(time)
            


        return time
    

