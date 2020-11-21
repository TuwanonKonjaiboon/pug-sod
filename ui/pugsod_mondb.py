import pymongo

client = pymongo.MongoClient()

mondb = client['pugsod']
collection = mondb['chat']

# {
#     users: {
#         user1: 1,
#         user2: 2
#     },
#     messages: [
#         {
#             msg: "Hello",
#             timestamp: 123123123,
#             sender: 0  # 0 = first,
#         }
#     ]
# }


class ChatDB:

    # user1 send msg to user2 return void
    # @param user1: user_id, user2: user_id, msg: string
    def insert_chat(self, user1: int, user2: int, msg: str):
        assert user1 != user2
        assert msg != ""

        if user1 > user2:
            user1, user2 = user2, user1

        result = collection.find(
            {"user.user1": user1, "user.user2": user2}, {"_id": 1})

        for x in result:
            print(x)

    def read_chat(self, user1: int, user2: int):
        result = collection.find(
            {"user.user1": user1, "user.user2": user2, "user.user2": {"$gt": user1}})


chatdb = ChatDB()
chatdb.insert_chat(1, 2, "hello")
