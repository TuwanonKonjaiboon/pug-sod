# This code is shit, but it's work (on my machine)

from tkinter import *

class ui:
    root = Tk()
    name = ""

    def __init__(self):
        ui.root.title("Pugsod")
        ui.root.geometry("400x400")
        ui.startPage()

    def clear():
        for element in ui.root.winfo_children():
            element.destroy()

    def startPage():
        welcome = Label(ui.root, text = "Welcome")
        welcome.pack()

        username_label = Label(ui.root, text = "username")
        username_label.pack()
        username = Entry(ui.root)
        username.pack()

        password_label = Label(ui.root, text = "password")
        password_label.pack()
        password = Entry(ui.root)
        password.pack()

        login_button = Button(ui.root, text ="login")
        login_button.pack()

        label = Label(ui.root, text = "", fg = "red")
        label.pack()

        login_button.config(command = lambda:ui.loginHandle(username.get(), password.get(), label))

    def loginHandle(username, password, label):
        #TODO query user_id and password
        if (password == "password"):
            ui.name = username
            ui.homePage()
            return
        label.config(text = "your password is incorrect")

    #home
    def homePage():
        ui.clear()
        welcome = Label(ui.root, text = "Welcome " + ui.name)
        welcome.pack()

        product_service = Button(ui.root, text = "product service", command = ui.productService)
        product_service.pack()

        customer_service = Button(ui.root, text = "customer service", command = ui.customerService)
        customer_service.pack()

        chat = Button(ui.root, text = "chat", command = ui.chatHandle)
        chat.pack()

    #productService
    def productService():
        ui.clear()

        create_product = Button(ui.root, text = "create new product", command = ui.newProduct)
        create_product.pack()

        view_product = Button(ui.root, text = "view products", command = ui.viewProductHandle)
        view_product.pack()
        
        back = Button(ui.root, text = "back", command = ui.homePage)
        back.pack()

    def newProduct():
        ui.clear()

        title_label = Label(ui.root, text = "title")
        title_label.pack()
        title = Entry(ui.root)
        title.pack()

        price_label = Label(ui.root, text = "price")
        price_label.pack()
        price = Entry(ui.root)
        price.pack()

        #TODO add all attribute
        
        create_button = Button(ui.root, text = "create", command = ui.createProductHandle)
        create_button.pack()

        back = Button(ui.root, text = "back", command = ui.productService)
        back.pack()

    def createProductHandle():
        #TODO
        return

    def viewProductHandle():
        ui.clear()
        #TODO get, update, delete product

        back = Button(ui.root, text = "back", command = ui.productService)
        back.pack()

    #customerService
    def customerService():
        ui.clear()
        search = Entry(ui.root)
        search.pack(pady = 10)
        search_button = Button(ui.root, text ="search", command = lambda:ui.searchHandle(search.get()))
        search_button.pack()

        cart = Button(ui.root, text = "item in cart", command = ui.cartHandle)
        cart.pack()

        back = Button(ui.root, text = "back", command = ui.homePage)
        back.pack()

    def searchHandle(keyword):
        ui.clear()

        #TODO query product info
        name = Label(ui.root, text = keyword)
        name.pack()
        
        add_to_cart = Button(ui.root, text = "add to cart", command = ui.createOrderItemHandle)
        add_to_cart.pack()

        back = Button(ui.root, text = "back", command = ui.customerService)
        back.pack()

    def createOrderItemHandle():
        #TODO
        return

    def cartHandle():
        ui.clear()

        #TODO get, delete orderItem

        back = Button(ui.root, text = "back", command = ui.customerService)
        back.pack()

    #chat
    def chatHandle():
        ui.clear()
        receiver = Entry(ui.root)
        receiver.pack()
        
        chat_button = Button(ui.root, text = "open chat room", command = lambda:ui.openChatroom(receiver.get(), label))
        chat_button.pack()

        back = Button(ui.root, text = "back", command = ui.homePage)
        back.pack()

        label = Label(ui.root, text = "", fg = "red")
        label.pack()
        
    def openChatroom(receiver, label):
        if (receiver == ""):
            label.config(text = "id is not valid")
            return
        #TODO query user_id
        
        ui.clear()
        back = Button(ui.root, text = "back", command = ui.homePage)
        back.pack()
        
        ui.chatroom(ui.root, ui.name, receiver)
        
        receiver_chat = Tk()
        receiver_chat.title(receiver + "'s chat")
        receiver_chat.geometry("400x400")
        
        ui.chatroom(receiver_chat, receiver, ui.name)
        receiver_chat.mainloop()

    def chatroom(parent, senader, receiver):
        message = Entry(parent)
        message.pack()

        send_button = Button(parent, text = "send", command = ui.sendHandle)
        send_button.pack()
        
        label = Label(parent, text = "send to " + receiver)
        label.pack()
        #TODO view messages

    def sendHandle():
        #TODO
        return
