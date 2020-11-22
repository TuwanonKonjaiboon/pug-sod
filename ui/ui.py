# This code is shit, but it's work (on my machine)

from tkinter import *
from tkinter import ttk
#from pugsod_mondb import chatdb


class ui:
    root = Tk()
    uid = 0
    name = ""

    products = [[0, "carrot", 50, 10, "peko peko", 2], [
        1, "shrimp", 100, 10, "a", 5], [2, "cucumber", 100, 10, "I hate cucumber", 1]]
    cart = []
    chat_message = "user0: Hello!\nuser1: Hello!\nuser0: How are You\nuser1: I'm horny"

    def __init__(self):
        ui.root.title("Pugsod")
        ui.root.geometry("400x400")
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

        Label(ui.root, text="id").pack()
        user_id = Entry(ui.root)
        user_id.pack()

        Label(ui.root, text="password").pack()
        password = Entry(ui.root, show="*")
        password.pack()

        ttk.Button(ui.root, text="login", command=lambda: ui.loginHandle(
            user_id.get(), password.get(), label)).pack()

        label = Label(ui.root, fg="red")
        label.pack()

    @staticmethod
    def loginHandle(user_id, password, label):
        if (not ui.representsInt(user_id)):
            label.config(text="id must be integer")
            return

        # TODO query user_id and password
        if (password == "password"):
            ui.uid = user_id
            ui.name = user_id
            ui.homePage()
            return
        label.config(text="your password is incorrect")

    # home
    @staticmethod
    def homePage():
        ui.clear()
        Label(ui.root, text="Welcome " + ui.name).pack()

        ttk.Button(ui.root, text="product service",
               command=ui.productService).pack()

        ttk.Button(ui.root, text="customer service",
               command=ui.customerService).pack()

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

        # TODO add new product to db
        ui.products.append([len(ui.products), title, price, amount, detail, 0])

        ui.productService()

    @staticmethod
    def viewProductHandle():
        ui.clear()
        # TODO query product
        for product in ui.products:
            ui.productDetail(product)

        ttk.Button(ui.root, text="back", command=ui.productService).pack()

    @staticmethod
    def productDetail(product):
        ratingText = "rating : "
        if int(product[5]) == 0:
            ratingText += "-"
        else:
            for i in range(product[5]):
                ratingText += "*"

        info = Label(ui.root, text=product[1] +
                     " " + str(product[2]) + "$ " + ratingText)
        info.pack()

        detail = Label(ui.root, text=product[4])
        detail.pack()

        ttk.Button(ui.root, text="delete", command=lambda: ui.deleteProductHandle(product[0])).pack()

    @staticmethod
    def deleteProductHandle(pid):
        # TODO delete product in db
        for i in range(len(ui.products)):
            if ui.products[i][0] == pid:
                ui.products.pop(i)
                break
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

        # TODO query product info
        product = None
        for i in range(len(ui.products)):
            if ui.products[i][1] == keyword:
                product = ui.products[i]
                break

        if product:
            label = Label(ui.root, text="", fg="red")
            label.pack()

            ratingText = "rating : "
            for i in range(product[5]):
                ratingText += "*"

            info = Label(
                ui.root, text=product[1] + " " + str(product[2]) + "$ " + ratingText)
            info.pack()

            detail = Label(ui.root, text=product[4])
            detail.pack()

            Label(ui.root, text="quantity").pack()
            quantity = Entry(ui.root)
            quantity.insert(INSERT, "1")
            quantity.pack()

            ttk.Button(ui.root, text="add to cart", command=lambda: ui.createItemHandle(
                product, quantity.get(), label)).pack()

            Label(ui.root, text="write your review here").pack()
            review = Entry(ui.root)
            review.pack()

            Label(ui.root, text="rating").pack()
            rating = Entry(ui.root)
            rating.pack()

            ttk.Button(ui.root, text="review", command=lambda: ui.reviewHandle(product, review.get(), rating.get(), label)).pack()
        else:
            label = Label(ui.root, text="404 product not founded")
            label.pack()
        ttk.Button(ui.root, text="back", command=ui.customerService).pack()

    @staticmethod
    def createItemHandle(product, quantity, label):
        if (not ui.representsInt(quantity)):
            label.config(text="quantity must be integer")
            return
        quantity = int(quantity)
        # if that the product is already in the cart already, update OrderItem. Else, add new OrderItem.
        chk = False
        for item in ui.cart:
            if item[3] == product[0]:
                if item[4] == ui.uid:
                    chk = True
                    break
        if chk:
            # TODO increase quantity
            item[1] += quantity
        else:
            # TODO insert orderItem
            # TODO add new orderItem to db
            ui.cart.append(
                [len(ui.cart), quantity, product[1], product[0], ui.uid])

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

        # TODO query orderItem
        for item in ui.cart:
            ui.orderItemDetail(item)

        ttk.Button(ui.root, text="back", command=ui.customerService).pack()

    @staticmethod
    def orderItemDetail(item):
        info = Label(ui.root, text=str(item[1]) + " " + item[2])
        info.pack()

        ttk.Button(ui.root, text="delete", command=lambda: ui.deleteItemHandle(item[0])).pack()

    @staticmethod
    def deleteItemHandle(oiid):
        # TODO delete product in db
        for i in range(len(ui.cart)):
            if ui.cart[i][0] == oiid:
                ui.cart.pop(i)
                break
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
        if (not ui.representsInt(receiver)):
            label.config(text="id must be integer")
            return
        receiver = int(receiver)
        # TODO query user_id
        if (False):
            label.config(text="id is not valid")
            return

        ui.clear()
        ttk.Button(ui.root, text="back", command=ui.homePage).pack()

        ui.chatroom(ui.root, ui.uid, receiver)

        receiver_chat = Tk()
        receiver_chat.title(str(receiver) + "'s chat")
        receiver_chat.geometry("400x400")

        ui.chatroom(receiver_chat, receiver, ui.uid)
        receiver_chat.mainloop()

    @staticmethod
    def chatroom(parent, sender, receiver):
        new_message = Entry(parent)
        new_message.pack()

        Label(parent, text="chat with user" + str(receiver)).pack()

        ttk.Button(parent, text="send", command=lambda: ui.sendHandle(new_message, sender, receiver)).pack()

        messages = Label(parent)
        messages.pack()
        ui.reloadMessages(messages)

    @staticmethod
    def sendHandle(message, sender, receiver):
        # TODO add chat message
        # chatdb.insert_chat(sender, receiver, message)
        #ui.chat_message += '\nuser' + str(sender) + ": " + message.get()

        message.delete('0', END)

    @staticmethod
    def reloadMessages(messages):
        # TODO query chat
        messages.config(text=ui.chat_message)
        messages.after(1000, lambda: ui.reloadMessages(messages))
