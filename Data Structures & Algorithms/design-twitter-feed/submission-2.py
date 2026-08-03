import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        self.follows[userId].add(userId)

        min_heap = []

        for ppl in self.follows[userId]:
            tweets = self.tweets.get(ppl)
            if tweets:
                idx = len(tweets) - 1
                time, tweetId = tweets[idx]
                # Use negative time for max-heap behavior with heapq
                heapq.heappush(min_heap, [-time, tweetId, ppl, idx - 1])
        
        while min_heap and len(res) < 10:
            neg_time, tweetId, ppl, idx = heapq.heappop(min_heap)
            res.append(tweetId)

            if idx >= 0:
                time, tweetId = self.tweets[ppl][idx]
                heapq.heappush(min_heap, [-time, tweetId, ppl, idx - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId != followerId:
            self.follows[followerId].discard(followeeId)