# This code is shit, but it's work (on my machine)

from tkinter import *

class ui:
    root = Tk()
    uid = 0
    name = ""
    
    products = [[0,"carrot", 50, 10, "peko peko", 2],[1,"shrimp", 100, 10, "a", 5],[2,"cucumber", 100, 10, "I hate cucumber", 1]]
    cart = [[0,9,"shrimp",1,0],[1,10,"carrot",0,0]]
    chat_message = "user0: Hello!\nuser1: Hello!\nuser0: How are You\nuser1: I'm horny"

    def __init__(self):
        ui.root.title("Pugsod")
        ui.root.geometry("400x400")
        ui.startPage()

    def representsInt(string):
        try: 
            int(string)
            return True
        except ValueError:
            return False

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

        label = Label(ui.root, fg = "red")
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
        price.insert(INSERT, "0")
        price.pack()

        amount_label = Label(ui.root, text = "amount")
        amount_label.pack()
        amount = Entry(ui.root)
        amount.insert(INSERT, "1")
        amount.pack()

        detail_label = Label(ui.root, text = "detail")
        detail_label.pack()
        detail = Entry(ui.root)
        detail.pack()
        
        create_button = Button(ui.root, text = "create", command = lambda:ui.createProductHandle(title.get(), int(price.get()), int(amount.get()), detail.get()))
        create_button.pack()

        back = Button(ui.root, text = "back", command = ui.productService)
        back.pack()

    def createProductHandle(title, price, amount, detail):

        #TODO add new product to db
        ui.products.append([len(ui.products),title,price,amount,detail,0])

        
        ui.productService()

    def viewProductHandle():
        ui.clear()
        #TODO query product
        for product in ui.products:
            ui.productDetail(product)
        
        back = Button(ui.root, text = "back", command = ui.productService)
        back.pack()

    def productDetail(product):
        ratingText = "rating : "
        if int(product[5]) == 0:
            ratingText += "-"
        else:
            for i in range(product[5]):
                ratingText += "*"
        
        info = Label(ui.root, text = product[1] + " " + str(product[2]) + "$ " + ratingText)
        info.pack()

        detail = Label(ui.root, text = product[4])
        detail.pack()

        delete = Button(ui.root, text = "delete", command = lambda:ui.deleteProductHandle(product[0]))
        delete.pack()

    def deleteProductHandle(pid):
        #TODO delete product in db
        for i in range(len(ui.products)):
            if ui.products[i][0] == pid:
                ui.products.pop(i)
                break
        ui.viewProductHandle()

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
        product = None
        for i in range(len(ui.products)):
            if ui.products[i][1] == keyword:
                product = ui.products[i]
                break

        if product:
            ratingText = "rating : "
            for i in range(product[5]):
                ratingText += "*"
            
            info = Label(ui.root, text = product[1] + " " + str(product[2]) + "$ " + ratingText)
            info.pack()

            detail = Label(ui.root, text = product[4])
            detail.pack()

            quantity = Label(ui.root, text = "quantity")
            quantity.pack()
            quantity = Entry(ui.root)
            quantity.insert(INSERT, "1")
            quantity.pack()
            
            add_to_cart = Button(ui.root, text = "add to cart", command = lambda:ui.createItemHandle(product, int(quantity.get())))
            add_to_cart.pack()
        else:
            label = Label(ui.root, text = "404 product not founded")
            label.pack()
        back = Button(ui.root, text = "back", command = ui.customerService)
        back.pack()

    def createItemHandle(product, quantity):
        #if that the product is already in the cart already, update OrderItem. Else, add new OrderItem.
        chk = False
        for item in ui.cart:
            if item[3] == product[0]:
                if item[4] == ui.uid:
                    chk = True
        if chk:
            #TODO increase quantity
            for item in ui.cart:
                if item[3] == product[0]:
                    if item[4] == ui.uid:
                        item[1] += quantity
        else:
            ui.cart.append([len(ui.cart),quantity,product[1],product[0],ui.uid]) #TODO add new orderItem to db
        
        ui.customerService();

    def cartHandle():
        ui.clear()

        #TODO query orderItem
        for item in ui.cart:
            ui.orderItemDetail(item)

        back = Button(ui.root, text = "back", command = ui.customerService)
        back.pack()

    def orderItemDetail(item):     
        info = Label(ui.root, text = str(item[1]) + " " + item[2])
        info.pack()

        delete = Button(ui.root, text = "delete", command = lambda:ui.deleteItemHandle(item[0]))
        delete.pack()

    def deleteItemHandle(oiid):
        #TODO delete product in db
        for i in range(len(ui.cart)):
            if ui.cart[i][0] == oiid:
                ui.cart.pop(i)
                break
        ui.cartHandle()

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
        if (not ui.representsInt(receiver)):
            label.config(text = "id must be integer")
            return

        #TODO query user_id
        if (False):
            label.config(text = "id is not valid")
            return
        
        ui.clear()
        back = Button(ui.root, text = "back", command = ui.homePage)
        back.pack()
        
        ui.chatroom(ui.root, ui.uid, int(receiver))
        
        receiver_chat = Tk()
        receiver_chat.title(receiver + "'s chat")
        receiver_chat.geometry("400x400")
        
        ui.chatroom(receiver_chat, int(receiver), ui.uid)
        receiver_chat.mainloop()

    def chatroom(parent, sender, receiver):
        new_message = Entry(parent)
        new_message.pack()

        label = Label(parent, text = "chat with user" + str(receiver))
        label.pack()

        send_button = Button(parent, text = "send", command = lambda:ui.sendHandle(new_message, sender, receiver))
        send_button.pack()
        
        messages = Label(parent)
        messages.pack()
        ui.reloadMessages(messages)

    def sendHandle(message, sender, receiver):
        #TODO add chat message
        ui.chat_message += '\nuser' + str(sender) + ": " + message.get()

        message.delete('0', END)

    def reloadMessages(messages):
        #TODO query chat
        messages.config(text = ui.chat_message)
        messages.after(1000, lambda:ui.reloadMessages(messages))


