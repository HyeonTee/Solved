class RecentCounter:
    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        # 유효한 범위 내의 핑만 남기기
        self.pings = [x for x in self.pings if x >= t - 3000]
        # 현재 핑 추가
        self.pings.append(t)
        return len(self.pings)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)