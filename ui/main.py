# from ui import *

# ui()
# ui.root.mainloop()
import asyncio
from services import UserProvider, ProductProvider, OrderItemProvider

userBloc = UserProvider()
prodBloc = ProductProvider()
oiBloc = OrderItemProvider()


async def main():

    # login user
    res = await userBloc.login('fubukichan@yahoo.com', 'qwerty123')
    if res[0] == 1:
        print(userBloc.user)
        print(res[1])
    else:
        print(res[1])

    # # create product
    # res = await prodBloc.create('test1', 'testDetail1', 10, 200)
    # print(res)

    # # read product
    # res = await prodBloc.read(size=5)
    # print(*res[1])

    # # update product
    # await prodBloc.update(11, product_title="new test 1")
    # await prodBloc.update(11, product_detail="new detail 1")
    # await prodBloc.update(11, price=200)
    # await prodBloc.update(11, amount=100)
    # await prodBloc.update(11, price=10, amount=50)
    # await prodBloc.update(1)  # error

    # # delete product
    # res = await prodBloc.delete_one_by_id(4)

    # # create OrderItem
    # await oiBloc.create(6, 100)

    # get all order items
    res = await oiBloc.get_all_order_items()
    print(*res[1], sep="\n")

    # # update order item quantity
    # await oiBloc.update_order_id(6, 1)
    # await oiBloc.update_order_id(7, 1)
    # """
    #     orderItem 8 is from another person who not the owner of payment of orders 1
    #     but it can be updated w/o constraint error
    # """
    # await oiBloc.update_order_id(8, 1)  # bug

    # # delete orderItem
    # await oiBloc.delete_one_by_id(8)

asyncio.run(main())
