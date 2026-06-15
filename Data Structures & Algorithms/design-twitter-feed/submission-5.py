class Twitter:

    def __init__(self):
        self.stack = []
        self.follows = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.stack.append([userId, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        print(self.follows, "\n", self.stack)
        return [s[1] for s in self.stack[::-1] if s[0] in self.follows[userId] or s[0] == userId][:10]
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
       if followeeId not in self.follows[followerId]: 
        self.follows[followerId].append(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
       if followeeId in self.follows[followerId]: 
        self.follows[followerId].remove(followeeId)
        
        
