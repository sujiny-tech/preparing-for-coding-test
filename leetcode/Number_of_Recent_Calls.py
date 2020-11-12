import collections

class RecentCounter:

    def __init__(self):
        self.l = collections.deque()

    def ping(self, t: int) -> int:
        self.l.append(t)

        while self.l[0] < t - 3000:
            self.l.popleft()

        return len(self.l)

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
param_1 = obj.ping(1)
param_2 = obj.ping(100)
param_3 = obj.ping(3001)
param_4 = obj.ping(3002)
print([obj, param_1, param_2, param_3, param_4])