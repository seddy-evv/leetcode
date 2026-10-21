# Task description:
# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see
# the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:
# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this
# function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in
# the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from
# most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID
# followeeId.

# Example 1:
# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]
# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should
# precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no
# longer following user 2.

# Constraints:
# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 104
# All the tweets have unique IDs.
# At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
# A user cannot follow himself.


# Max-Heap via Min-Heap Inversion (K-Way Merge / Timeline Interleaving) combined with Hash Map of Hash Sets.
import heapq
from collections import defaultdict


class Twitter:

    def __init__(self):
        """Initializes the Twitter object."""
        # Global timestamp counter to track absolute post chronological order
        self.time = 0
        # Map user to a list of tuples: userId -> [(timestamp, tweetId), ...]
        self.tweets = defaultdict(list)
        # Map user to a set of followed users: followerId -> {followeeId1, followeeId2, ...}
        self.followees = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """Composes a new tweet by the user."""
        # Increment global time to simulate sequential chronological ticks
        self.time += 1
        # Store time as negative to use Python's min-heap as a max-heap for recent tweets
        self.tweets[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        """Retrieves the 10 most recent tweet IDs in the user's news feed."""
        min_heap = []

        # A user always follows themselves implicitly to see their own tweets
        users_to_check = self.followees[userId] | {userId}

        for u in users_to_check:
            if u in self.tweets:
                # Get the last index of the user's tweet history array
                last_idx = len(self.tweets[u]) - 1
                neg_time, tweet_id = self.tweets[u][last_idx]

                # Push a tuple containing: (negative_timestamp, tweet_id, user_id, index_of_next_older_tweet)
                heapq.heappush(min_heap, (neg_time, tweet_id, u, last_idx - 1))

        result = []
        # Extract up to 10 most recent tweets chronologically
        while min_heap and len(result) < 10:
            neg_time, tweet_id, u, next_idx = heapq.heappop(min_heap)
            result.append(tweet_id)

            # If the same user has older tweets left, push the next one into the heap
            if next_idx >= 0:
                older_neg_time, older_tweet_id = self.tweets[u][next_idx]
                heapq.heappush(min_heap, (older_neg_time, older_tweet_id, u, next_idx - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """The user with ID followerId started following the user with ID followeeId."""
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """The user with ID followerId started unfollowing the user with ID followeeId."""
        self.followees[followerId].discard(followeeId)


if __name__ == "__main__":
    twitter = Twitter()

    # User 1 posts a tweet (id = 5)
    twitter.postTweet(1, 5)
    print(f"User 1 Feed: {twitter.getNewsFeed(1)}")
    # Output: [5]

    # User 1 follows User 2
    twitter.follow(1, 2)

    # User 2 posts a tweet (id = 6)
    twitter.postTweet(2, 6)

    # User 1 checks feed (should see User 2's tweet first, then their own)
    print(f"User 1 Feed after following User 2: {twitter.getNewsFeed(1)}")
    # Output: [6, 5]

    # User 1 unfollows User 2
    twitter.unfollow(1, 2)
    print(f"User 1 Feed after unfollowing User 2: {twitter.getNewsFeed(1)}")
    # Output: [5]


# • Time Complexity:
# 	- postTweet(): O(1) constant time lookup and insertion into the list mapping.
# 	- getNewsFeed(): O(FlogF) in the absolute worst case, or O(F + KlogF) where F is the number of followees a user
# 	tracks and K = 10 is the fixed constant limit. Building the initial heap takes O(F) steps. Popping the top element
# 	up to 10 times and reorganizing the heap with another item takes 10*O(log F), making execution highly scalable when
# 	accounts have lengthy histories.
# 	- follow() / unfollow(): O(1) average time to modify standard hash set elements.
# • Space Complexity: O(T + F_total) auxiliary space overall, where T is the absolute aggregate volume of total
# tweets submitted to the platform and F_total tracks the universal map of following relationships established across
# all global user structures.
