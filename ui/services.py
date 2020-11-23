import asyncio

from pugsod_mydb import UserDB, ProductDB, OrderItemDB
from model import UserDAO, ProductDAO, OrderItemDAO


class UserProvider:

    user = None

    def __init__(self):
        self.userdb = UserDB()

    # log user in
    def login(self, email, password):
        res = self.userdb.login(email, password)

        # if success, set user
        if res['status'] == 1:
            usr = res['data']
            UserProvider.user = UserDAO(
                id=usr[0],
                name=usr[1]+" "+usr[2],
                email=usr[3],
                picURL=usr[5]
            )
            return (1, 'user logged in')

        return (0, 'login fail!')

    # log user out
    def logout(self):
        UserProvider.user = None
        return (1, 'user logged out')


class ProductProvider:

    def __init__(self):
        self.proddb = ProductDB()

    def create(self, product_title="", product_detail="", price=0, amount=0):

        # not login
        if UserProvider.user == None:
            return (0, 'user not login')
        # insert product into database
        res = self.proddb.createDB(
            UserProvider.user.id,
            product_title,
            product_detail,
            price,
            amount
        )

        if res['status'] == 1:
            return (1, f'product {product_title} was added!')
        else:
            return (0, f'product add fail...')

    def read(self, size=None):

        # user not login
        if UserProvider.user == None:
            return (0, 'user not login')

        res = self.proddb.readDB(size=size, seller_id=UserProvider.user.id)

        if res['status'] == 1:
            return (1, [ProductDAO(
                id=prd[0],
                sellerId=prd[1],
                name=prd[2],
                detail=prd[3],
                price=prd[4],
                amount=prd[5],
                rating=prd[6],
                update_at=prd[7]
            ) for prd in res['data']])
        else:
            return (0, 'read products fail...')

    def update(self, product_id, **values):
        """
            what you can update: \n
            product_title: str, \n
            product_detail: str, \n
            price: int, \n
            amount: int, \n
        """

        res = self.proddb.updateDB(product_id, **values)

        if res['status'] == 1:
            return (1, f"product id:{product_id} updated!")
        return (0, f"product id:{product_id} update fail...")

    def delete_one_by_id(self, product_id):
        res = self.proddb.deleteDB(product_id=product_id)

        if res['status'] == 1:
            return (1, [])
        else:
            return (0, [])
            
    def search(self, query="", size=None):
        # user not login
        if UserProvider.user == None:
            return (0, 'user not login')

        res = self.proddb.searchDB(query=query, size=size)

        if res['status'] == 1:
            return (1, [ProductDAO(
                id=prd[0],
                sellerId=prd[1],
                name=prd[2],
                detail=prd[3],
                price=prd[4],
                amount=prd[5],
                rating=prd[6],
                update_at=prd[7]
            ) for prd in res['data']])
        else:
            return (0, 'read products fail...')
            
    def read_id(self, product_id, size=None):

        # user not login
        if UserProvider.user == None:
            return (0, 'user not login')

        res = self.proddb.readDB(size=size, product_id=product_id)

        if res['status'] == 1:
            return (1, [ProductDAO(
                id=prd[0],
                sellerId=prd[1],
                name=prd[2],
                detail=prd[3],
                price=prd[4],
                amount=prd[5],
                rating=prd[6],
                update_at=prd[7]
            ) for prd in res['data']])
        else:
            return (0, 'read products fail...')


class OrderItemProvider:

    def __init__(self):
        self.oidb = OrderItemDB()

    def create(self, product_id, quantity):

        # not login
        if UserProvider.user == None:
            return (0, 'user not login')

        user_id = UserProvider.user.id

        res = self.oidb.createDB(user_id, product_id, quantity)

        if res['status'] == 1:
            return (1, 'create order item success!')
        else:
            return (0, 'create order item fail...')

    def get_all_order_items(self):

        if UserProvider.user == None:
            return (0, 'user not login')

        res = self.oidb.readDB(customer_id=UserProvider.user.id)

        if res['status'] == 1:
            return (1, [
                OrderItemDAO(id=od[0], custId=od[1], prodId=od[2], orderId=od[3], quantity=od[4]) for od in res['data']
            ])
        else:
            return (0, [])
            
    def get_order_item(self, product_id):

        if UserProvider.user == None:
            return (0, 'user not login')

        res = self.oidb.readDB(customer_id=UserProvider.user.id, product_id=product_id)

        if res['status'] == 1:
            return (1, [
                OrderItemDAO(id=od[0], custId=od[1], prodId=od[2], orderId=od[3], quantity=od[4]) for od in res['data']
            ])
        else:
            return (0, [])

    def update_quantity(self, orderItem_id, quantity):
        # not login
        if UserProvider.user == None:
            return (0, 'user not login')

        res = self.oidb.updateDB(orderItem_id, quantity=quantity)

        if res['status'] == 1:
            return (1, 'order item updated')
        else:
            return (0, 'update fail...')

    def update_order_id(self, orderItem_id, order_id):
        # not login
        if UserProvider.user == None:
            return (0, 'user not login')

        res = self.oidb.updateDB(orderItem_id, order_id=order_id)

        if res['status'] == 1:
            return (1, 'order item updated')
        else:
            return (0, 'update fail...')

    def delete_one_by_id(self, orderItem_id):
        # not login
        if UserProvider.user == None:
            return (0, 'user not login')
        
        res = self.oidb.deleteDB(orderItem_id=orderItem_id)

        if res['status'] == 1:
            return (1, [
                OrderItemDAO(id=od[0], custId=od[1], prodId=od[2], orderId=od[3], quantity=od[4]) for od in res['data']
            ])
        else:
            return (0, [])
