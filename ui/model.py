class Chat:
    def __init__(self, userId1, userId2, messages):
        self.userId1 = userId1
        self.userId2 = userId2
        self.messages = messages


class Message:
    def __init__(self, msg, timestamp, sender):
        self.msg = msg
        self.timestamp = timestamp
        self.sender = sender
