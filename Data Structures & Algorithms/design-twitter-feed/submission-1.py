import heapq

class Twitter:

    def __init__(self):
        self.followMap = {}
        self.tweetMap = {}
        self.timestamp = 0
    
    def user(self, userId: int) -> None:
        if userId not in self.followMap.keys():
            self.followMap[userId] = {userId}
        if userId not in self.tweetMap.keys():
            self.tweetMap[userId] = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user(userId)
        self.tweetMap[userId].append([self.timestamp, tweetId])
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.user(userId)
        feed = []
        for i in self.followMap[userId]:
            feed += self.tweetMap[i]
        feed.sort(key=lambda x: x[0])
        res = []
        for _ in range(min(10, len(feed))):
            res.append(feed.pop()[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user(followerId)
        self.user(followeeId)
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap and followerId != followeeId:
            self.followMap[followerId].discard(followeeId)