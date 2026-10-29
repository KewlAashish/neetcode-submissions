class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.user_posts = defaultdict(lambda: deque(maxlen=10))
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_posts[userId].append([self.t, tweetId])
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # inside a max heap of size 10 insert all the posts from the users which the userId follows
        heap = []
        users_to_check = self.following[userId] | {userId}

        for user_id in users_to_check:
            posts = self.user_posts[user_id]

            posts = reversed(posts)

            for post in posts:
                post_time, post_id = post[0], post[1]

                # if worth checking posts?
                if (heap and len(heap) >= 10) and heap[0][0] >= post_time:
                    # the oldest post of the user feed till now is more recent then this user remaining post list, no need to iterate and also the fact that our heap already has 10 posts
                    break
                
                if len(heap) == 10:
                    heapq.heappushpop(heap, [post_time, post_id])
                else:
                    heapq.heappush(heap, [post_time, post_id])

        feed = []
        while heap:
            item = heapq.heappop(heap)
            feed.append(item[1])

        return feed[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        return
