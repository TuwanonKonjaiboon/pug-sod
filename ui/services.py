import asyncio

from pugsod_mydb import UserDB, ProductDB, OrderItemDB
from model import UserDAO, ProductDAO, OrderItemDAO


class UserProvider:

    user = None

    def __init__(self):
        self.userdb = UserDB()

    # log user in
    async def login(self, email, password):
        res = await self.userdb.login(email, password)

        # if success, set user
        if res['status'] == 1:
            usr = res['data']
            UserProvider.user = UserDAO(
                id=usr[0],
                name=usr[1]+usr[2],
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

    async def create(self, product_title="", product_detail="", price=0, amount=0):

        # not login
        if UserProvider.user == None:
            return (0, 'user not login')

        # insert product into database
        res = await self.proddb.createDB(
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

    async def read(self, query="", size=None):

        # user not login
        if UserProvider.user == None:
            return (0, 'user not login')

        res = await self.proddb.readDB(query=query, size=size)

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

    async def update(self, product_id, **values):
        """
            what you can update: \n
            product_title: str, \n
            product_detail: str, \n
            price: int, \n
            amount: int, \n
        """

        res = await self.proddb.updateDB(product_id, **values)

        if res['status'] == 1:
            return (1, f"product id:{product_id} updated!")
        return (0, f"product id:{product_id} update fail...")

    async def delete_one_by_id(self, product_id):
        res = await self.proddb.deleteDB(product_id)

        if res['status'] == 1:
            return (1, res['msg'], [ProductDAO(*prd) for prd in res['data']])
        else:
            return (0, [])


class OrderItemProvider:

    def __init__(self):
        self.oidb = OrderItemDB()

    async def create(self, product_id, quantity):

        # not login
        if UserProvider.user == None:
            return (0, 'user not login')

        user_id = UserProvider.user.id

        res = await self.oidb.createDB(user_id, product_id, quantity)

        if res['status'] == 1:
            return (1, 'create order item success!')
        else:
            return (0, 'create order item fail...')

    async def get_all_order_items(self):

        if UserProvider.user == None:
            return (0, 'user not login')

        res = await self.oidb.readDB(customer_id=UserProvider.user.id)

        print(*res['data'], sep='\n')

        if res['status'] == 1:
            return (1, [
                OrderItemDAO(id=od[0], custId=od[1], prodId=od[2], orderId=od[3], quantity=od[4]) for od in res['data']
            ])
        else:
            return (0, [])

    async def update_quantity(self, orderItem_id, quantity):
        # not login
        if UserProvider.user == None:
            return (0, 'user not login')

        res = await self.oidb.updateDB(orderItem_id, quantity=quantity)

        if res['status'] == 1:
            return (1, 'order item updated')
        else:
            return (0, 'update fail...')

    async def update_order_id(self, orderItem_id, order_id):
        # not login
        if UserProvider.user == None:
            return (0, 'user not login')

        res = await self.oidb.updateDB(orderItem_id, order_id=order_id)

        if res['status'] == 1:
            return (1, 'order item updated')
        else:
            return (0, 'update fail...')

    async def delete_one_by_id(self, orderItem_id):
        # not login
        if UserProvider.user == None:
            return (0, 'user not login')

        res = await self.oidb.deleteDB(orderItem_id=orderItem_id)

        if res['status'] == 1:
            return (1, [
                OrderItemDAO(id=od[0], custId=od[1], prodId=od[2], orderId=od[3], quantity=od[4]) for od in res['data']
            ])
        else:
            return (0, [])
