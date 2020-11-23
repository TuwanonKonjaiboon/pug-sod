from tkinter import *
from tkinter import ttk
import copy

from pugsod_mondb import chatdb
from services import UserProvider, ProductProvider, OrderItemProvider

userBloc = UserProvider()
prodBloc = ProductProvider()
oiBloc = OrderItemProvider()

class ui:
    root = Tk()

    def __init__(self):
        ui.root.title("Pugsod")
        ui.root.geometry("400x600")
        ui.startPage()

    @staticmethod
    def representsInt(string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    @staticmethod
    def clear():
        for element in ui.root.winfo_children():
            element.destroy()

    @staticmethod
    def startPage():
        ui.clear()

        Label(ui.root, text="Welcome").pack()

        Label(ui.root, text="username").pack()
        username = Entry(ui.root)
        username.pack()

        Label(ui.root, text="password").pack()
        password = Entry(ui.root, show="*")
        password.pack()

        ttk.Button(ui.root, text="login", command=lambda: ui.loginHandle(
            username.get(), password.get(), label)).pack()

        label = Label(ui.root, fg="red")
        label.pack()

    @staticmethod
    def loginHandle(username, password, label):
        res = userBloc.login(username, password)
        if res[0]:
            ui.homePage()
            return
        label.config(text="id or password is incorrect")

    # home
    @staticmethod
    def homePage():
        ui.clear()
        Label(ui.root, text="Hi " + userBloc.user.name).pack()

        product_service = ttk.Button(ui.root, text="product service", command=ui.productService)
        product_service.pack()

        customer_service = ttk.Button(ui.root, text="customer service",
               command=ui.customerService)
        customer_service.pack()

        ttk.Button(ui.root, text="chat", command=ui.chatHandle).pack()
        ttk.Button(ui.root, text="logout", command=ui.startPage).pack()

    # productService
    @staticmethod
    def productService():
        ui.clear()
        ttk.Button(ui.root, text="create new product", command=ui.newProduct).pack()
        ttk.Button(ui.root, text="view products",
                              command=ui.viewProductHandle).pack()
        ttk.Button(ui.root, text="back", command=ui.homePage).pack()

    @staticmethod
    def newProduct():
        ui.clear()

        Label(ui.root, text="title").pack()
        title = Entry(ui.root)
        title.pack()

        Label(ui.root, text="price").pack()
        price = Entry(ui.root)
        price.insert(INSERT, "0")
        price.pack()

        Label(ui.root, text="amount").pack()
        amount = Entry(ui.root)
        amount.insert(INSERT, "1")
        amount.pack()

        Label(ui.root, text="detail").pack()
        detail = Entry(ui.root)
        detail.pack()

        ttk.Button(ui.root, text="create", command=lambda: ui.createProductHandle(title.get(), int(price.get()), int(amount.get()), detail.get())).pack()
        ttk.Button(ui.root, text="back", command=ui.productService).pack()

    @staticmethod
    def createProductHandle(title, price, amount, detail):
        prodBloc.create(title, detail, int(price), int(amount))
        ui.productService()

    @staticmethod
    def viewProductHandle():
        ui.clear()
        res = prodBloc.read(size = 7)
        if res[0]:
            for product in res[1]:
                ui.productDetail(product)

        ttk.Button(ui.root, text="back", command=ui.productService).pack()

    @staticmethod
    def productDetail(product):
        ratingText = "rating : "
        if int(product.rating) == 0:
            ratingText += "-"
        else:
            for i in range(int(product.rating)):
                ratingText += "*"

        info = Label(ui.root, text=product.name +
                     " " + str(product.price) + "$ " + ratingText)
        info.pack()

        detail = Label(ui.root, text=product.detail)
        detail.pack()

        ttk.Button(ui.root, text="delete", command=lambda: ui.deleteProductHandle(product.id)).pack()

    @staticmethod
    def deleteProductHandle(pid):
        prodBloc.delete_one_by_id(pid)
        ui.viewProductHandle()

    # customerService
    @staticmethod
    def customerService():
        ui.clear()
        
        search = Entry(ui.root)
        search.pack(pady=10)
        
        ttk.Button(ui.root, text="search",command=lambda: ui.searchHandle(search.get())).pack()
        ttk.Button(ui.root, text="item in cart", command=ui.cartHandle).pack()
        ttk.Button(ui.root, text="back", command=ui.homePage).pack()

    @staticmethod
    def searchHandle(keyword):
        ui.clear()
        res = prodBloc.search(query = keyword, size = 10)
        #  It works, Don't touch it
        if res[1]:
            if len(res[1]) > 0:
                ttk.Button(ui.root, text=res[1][0].name, command=lambda: ui.veiwResult(res[1][0])).pack()
            if len(res[1]) > 1:
                ttk.Button(ui.root, text=res[1][1].name, command=lambda: ui.veiwResult(res[1][1])).pack()
            if len(res[1]) > 2:
                ttk.Button(ui.root, text=res[1][2].name, command=lambda: ui.veiwResult(res[1][2])).pack()
            if len(res[1]) > 3:
                ttk.Button(ui.root, text=res[1][3].name, command=lambda: ui.veiwResult(res[1][3])).pack()
            if len(res[1]) > 4:
                ttk.Button(ui.root, text=res[1][4].name, command=lambda: ui.veiwResult(res[1][4])).pack()
            if len(res[1]) > 5:
                ttk.Button(ui.root, text=res[1][5].name, command=lambda: ui.veiwResult(res[1][5])).pack()
            if len(res[1]) > 6:
                ttk.Button(ui.root, text=res[1][6].name, command=lambda: ui.veiwResult(res[1][6])).pack()
            if len(res[1]) > 7:
                ttk.Button(ui.root, text=res[1][7].name, command=lambda: ui.veiwResult(res[1][7])).pack()
            if len(res[1]) > 8:
                ttk.Button(ui.root, text=res[1][8].name, command=lambda: ui.veiwResult(res[1][8])).pack()
            if len(res[1]) > 9:
                ttk.Button(ui.root, text=res[1][9].name, command=lambda: ui.veiwResult(res[1][9])).pack()
        else:
            label = Label(ui.root, text="404 product not founded")
            label.pack()
        ttk.Button(ui.root, text="back", command=ui.customerService).pack()

    @staticmethod
    def veiwResult(product):
        ui.clear()
        label = Label(ui.root, text="", fg="red")
        label.pack()

        ratingText = "rating : "
        if int(product.rating) == 0:
            ratingText += "-"
        else:
            for i in range(int(product.rating)):
                ratingText += "*"

        info = Label(
            ui.root, text=product.name + " " + str(product.price) + "$ " + ratingText)
        info.pack()

        Label(ui.root, text=product.detail).pack()

        Label(ui.root, text="quantity").pack()
        quantity = Entry(ui.root)
        quantity.insert(INSERT, "1")
        quantity.pack()

        ttk.Button(ui.root, text="add to cart", command=lambda: ui.createItemHandle(
            product, quantity.get(), label)).pack()

        # TODO soon
        #Label(ui.root, text="write your review here").pack()
        #review = Entry(ui.root)
        #review.pack()

        #Label(ui.root, text="rating").pack()
        #rating = Entry(ui.root)
        #rating.pack()

        #ttk.Button(ui.root, text="review", command=lambda: ui.reviewHandle(product, review.get(), rating.get(), label)).pack()
        ttk.Button(ui.root, text="back", command=ui.customerService).pack()
        
    @staticmethod
    def createItemHandle(product, quantity, label):
        if (not ui.representsInt(quantity)):
            label.config(text="quantity must be integer")
            return
        quantity = int(quantity)
        # if that the product is already in the cart already, update OrderItem. Else, add new OrderItem.
        chk = False
        res = oiBloc.get_order_item(product.id)
        if res[1]:
            oiBloc.update_quantity(res[1][0].id, res[1][0].quantity + quantity)
        else:
            oiBloc.create(product.id, quantity)

        ui.customerService()

    @staticmethod
    def reviewHandle(product, reveiw, rating, label):
        if (not ui.representsInt(rating)):
            label.config(text="rating must be integer")
            return
        rating = int(rating)
        # TODO create new reveiw

        ui.customerService()

    @staticmethod
    def cartHandle():
        ui.clear()
        res = oiBloc.get_all_order_items()
        for item in res[1]:
            ui.orderItemDetail(item)

        ttk.Button(ui.root, text="back", command=ui.customerService).pack()

    @staticmethod
    def orderItemDetail(item):
        res = prodBloc.read_id(item.prodId, size = 1)
        info = Label(ui.root, text=str(item.quantity) + " " + res[1][0].name)
        info.pack()

        ttk.Button(ui.root, text="delete", command=lambda: ui.deleteItemHandle(item.id)).pack()

    @staticmethod
    def deleteItemHandle(oiid):
        oiBloc.delete_one_by_id(oiid)
        ui.cartHandle()

    # chat
    @staticmethod
    def chatHandle():
        ui.clear()
        receiver = Entry(ui.root)
        receiver.pack()

        ttk.Button(ui.root, text="open chat room", command=lambda: ui.openChatroom(receiver.get(), label)).pack()
        ttk.Button(ui.root, text="back", command=ui.homePage).pack()

        label = Label(ui.root, text="", fg="red")
        label.pack()

    @staticmethod
    def openChatroom(receiver, label):
        if not ui.representsInt(receiver):
            label.config(text="id must be integer")
            return
        receiver = int(receiver)
        if receiver == userBloc.user.id:
            label.config(text="you can't chat with yourself")
            return

        ui.clear()
        ttk.Button(ui.root, text="back", command=ui.chatHandle).pack()

        ui.chatroom(ui.root, userBloc.user.id, receiver)

        receiver_chat = Tk()
        receiver_chat.title(str(receiver) + "'s chat")
        receiver_chat.geometry("400x400")

        ui.chatroom(receiver_chat, receiver, userBloc.user.id)
        receiver_chat.mainloop()

    @staticmethod
    def chatroom(parent, sender, receiver):
        new_message = Entry(parent)
        new_message.pack()

        Label(parent, text="chat with user" + str(receiver)).pack()

        ttk.Button(parent, text="send", command=lambda: ui.sendHandle(new_message, sender, receiver)).pack()

        messages = Label(parent)
        messages.pack()
        ui.reloadMessages(messages, sender, receiver)

    @staticmethod
    def sendHandle(message, sender, receiver):
        chatdb.insert_chat(sender, receiver, message.get())

        message.delete('0', END)

    @staticmethod
    def reloadMessages(message_label, sender, receiver):
        message_text = ""
        chat_messages = chatdb.read_chat(sender, receiver)
        if chat_messages:
            for m in chat_messages:
                message_text += "user" + str(m.sender) + ": " + m.msg + "\n"
        
        message_label.config(text = message_text)
        message_label.after(1000, lambda: ui.reloadMessages(message_label, sender, receiver))
