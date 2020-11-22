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


class UserDAO:
    def __init__(self, id, name, email, picURL):
        self.id = id
        self.name = name
        self.email = email
        self.picURL = picURL

    def __str__(self):
        return f"User id: {self.id}, name: {self.name}, email: {self.email}, picURL: {self.picURL}"


class ProductDAO:
    def __init__(self, id, sellerId, name, detail, price, amount, rating, update_at):
        self.id = id
        self.sellerId = sellerId
        self.name = name
        self.detail = detail
        self.price = price
        self.amount = amount
        self.rating = rating
        self.update_at = update_at

    def __repr__(self):
        return f"Product id: {self.id} name: {self.name} detail: {self.detail} rating: {self.rating}"

    def __str__(self):
        return f"Product id: {self.id} name: {self.name} detail: {self.detail} rating: {self.rating}"


class OrderItemDAO:
    def __init__(self, id, custId, prodId, quantity, orderId=None):
        self.id = id
        self.custId = custId
        self.prodId = prodId
        self.orderId = orderId
        self.quantity = quantity

    def __repr__(self):
        return f"OrderItem id: {self.id}, custId: {self.custId}, prodId: {self.prodId}, orderId: {self.orderId} quantity: {self.quantity}"

    def __str__(self):
        return f"OrderItem id: {self.id}, custId: {self.custId}, prodId: {self.prodId}, orderId: {self.orderId} quantity: {self.quantity}"
