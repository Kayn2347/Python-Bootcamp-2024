class Youtube:
    def __init__(self, username, subscribers=0):
        self.username = username
        self.subscribers = subscribers


class Twitter:
    def __init__(self, username, followers=0):
        self.username = username
        self.followers = followers


youtube_user1 = Youtube("kayn")
twitter_user1 = Twitter("Chisee")

youtube_user2 = Youtube("Chisee")
twitter_user2 = Twitter("kayn")

print(isinstance(twitter_user1, Twitter))
print(isinstance(twitter_user1, object))

