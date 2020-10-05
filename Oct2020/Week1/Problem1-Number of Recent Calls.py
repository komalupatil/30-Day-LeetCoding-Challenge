#Problem1

#Leetcode 933. Number of Recent Calls

#Solution - queue

class RecentCounter:

    def __init__(self):
        self.time = []
        

    def ping(self, t: int) -> int:
        counter = 0
        self.time.append(t)
        while self.time[0] < t-3000:
            del self.time[0]

        return len(self.time)
        
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)