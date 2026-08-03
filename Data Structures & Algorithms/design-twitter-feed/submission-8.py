from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        self.following[userId].add(userId)
        heap = []
        for ppl in self.following[userId]:
            tweets = self.tweets.get(ppl)
            if tweets:
                for i in range(len(tweets)):
                    time, tweetId = tweets[i]
                    heapq.heappush_max(heap, [time, tweetId])
        while heap and len(res) < 10:
            time, tweetId = heapq.heappop_max(heap)
            res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followerId != followeeId:
            self.following[followerId].discard(followeeId)