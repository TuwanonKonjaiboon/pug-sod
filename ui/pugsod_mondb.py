import time
from typing import List, Mapping
from pymongo import MongoClient
from pymongo.errors import OperationFailure

from model import Chat, Message

client = MongoClient()
collection = client['pugsod']['chat']


class ChatDB:

    @classmethod
    def _current_milli_time(cls) -> int: return int(round(time.time() * 1000))
    # user1 send msg to user2 return void
    # @param user1: user_id, user2: user_id, msg: string

    def insert_chat(self, senderId: int, receiverId: int, msg: str) -> List[Message]:

        try:
            client = MongoClient()
            collection = client['pugsod']['chat']
            assert senderId != receiverId
            assert msg != ""

            user1, user2 = senderId, receiverId

            if user1 > user2:
                user1, user2 = user2, user1

            chat = {
                'msg': msg,
                'timestamp': ChatDB._current_milli_time(),
                'sender': senderId
            }

            collection.update_one({'user.user1': user1, 'user.user2': user2}, {
                '$push': {'messages': chat}}, True)

            retmsg = ['1', 'update success']
        except:
            retmsg = ['0', 'update fail']
        finally:
            return retmsg

    def read_chat(self, userId1: int, userId2: int):
        try:
            assert userId1 != userId2

            result = collection.find_one(
                {'user.user1': userId1, 'user.user2': userId2})

            retval: List[Message] = sorted([
                Message(**obj) for obj in result['messages']
            ], key=lambda o: o.timestamp)
        except:
            retval = None
        finally:
            return retval


chatdb = ChatDB()

# # Example read
val = chatdb.read_chat(1, 2)
for x in val:
    print(x.timestamp)

# # Example
# chatdb.insert_chat(1, 2, "Hello! 2")
# chatdb.insert_chat(2, 1, "Hi 1")
# chatdb.insert_chat(1, 2, "How are you?")
# chatdb.insert_chat(3, 2, "FAQ!!!")
# chatdb.insert_chat(2, 1, "I'm fine!")
