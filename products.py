from tkinter import messagebox
import pyodbc
from tkinter import *

#Set colors to be used
color = "#d9d7d7"
red = "#FF4C4C"
gray = "#A0A0A0"
light = "#F5F5F5"

#Database Connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MARUNDAN\SQLEXPRESS;'
                      'Database=DB_Inventory;'
                      'Trusted_Connection=yes;')

#Identifier of the item to be updated
global toUpdate
toUpdate = 0

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity


def addProduct():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    if e1.get() == "" or len(e1.get()) < 3:
        messagebox.showinfo("Login Error", "Input a valid product name. (Atleast 3 letters)")
    elif e2.get() == "" and e2.get().isnumeric():
        messagebox.showinfo("Login Error", "Input a valid price.")
    elif e3.get() == "" and e3.get().isnumeric:
        messagebox.showinfo("Login Error", "Input a valid quantity.")
    elif e2.get().isnumeric and e3.get().isnumeric():
        product = Product(e1.get(), e2.get(), e3.get())
        cursor.execute(
            "INSERT INTO items (product_name, price, quantity) VALUES" + "('" + product.getName() + "'," + product.getPrice() + "," + product.getQuantity() + ")")
        prod = cursor.execute('SELECT * FROM items')
        cursor.commit()
        root.geometry("435x600")
        viewProducts()
    else:
        messagebox.showinfo("Login Error", "The price and quantity must be numeric.")

def deleteProduct(product):
    cursor = conn.cursor()
    print(product)
    cursor.execute("DELETE FROM items WHERE id = "+ str(product))
    normalizeButtons(True)
    cursor.commit()
    viewProducts()


def updateProduct(product):
    global toUpdate
    toUpdate = product
    normalizeButtons(False)
    viewProducts()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    name = ""
    price = 0
    qty = 0
    cursor = conn.cursor()
    prod = cursor.execute("SELECT * FROM items WHERE id = " + str(product))
    for a in cursor.fetchall():
        name = a[1]
        price = a[2]
        qty = a[3]
    e1.insert(0, str(name))
    e2.insert(0, str(price))
    e3.insert(0, str(prod))
    cursor.commit()
    viewProducts()
    btn1.configure(command=lambda: updateMyself(e1.get(), e2.get(), e3.get(), product))


def updateMyself(name, price, quantity, id):
    global toUpdate
    if name == "" or len(e1.get()) < 3:
        messagebox.showinfo("Login Error", "Input a valid product name. (Atleast 3 letters)")
    elif price == "":
        messagebox.showinfo("Login Error", "Input a price.")
    elif id == "":
        messagebox.showinfo("Login Error", "Input quantity.")
    else:
        cursor = conn.cursor()
        cursor.execute("UPDATE items " +
                       "SET product_name = '" + name + "', price = " + price + ", quantity = " + quantity +
                       "WHERE id = " + str(id))
        cursor.commit()
        normalizeButtons(True)
        toUpdate = ""
        viewProducts()

def cancelUpdate():
    global toUpdate
    normalizeButtons(True)
    toUpdate = 0
    viewProducts()

def windowExtender():
    cursor = conn.cursor()
    cursor.execute("select * from items")
    root.geometry("435x" + str(200 + (len(cursor.fetchall()) * 36)))
    cursor.commit()

def normalizeButtons(tralse):
    if tralse:
        btn1['background'] = gray
        btn2['background'] = light
        btn3['background'] = gray
        btn1['state'] = DISABLED
        btn2['state'] = NORMAL
        btn3['state'] = DISABLED
    else:
        btn1['background'] = light
        btn2['background'] = gray
        btn3['background'] = light
        btn1['state'] = NORMAL
        btn2['state'] = DISABLED
        btn3['state'] = NORMAL

def viewProducts():
    global toUpdate
    windowExtender()
    row = 1
    list = separator.grid_slaves()
    for l in list:
        l.destroy()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")

    addHeaders()
    for prod in cursor.fetchall():
        if toUpdate == prod[0]:
            Label(separator, text=prod[1], background=red, width=10).grid(row=row, column=0,
                                                                            sticky=W + E + N + S, padx=10, pady=5)
            Label(separator, text=prod[2], background=red, width=10).grid(row=row, column=1,
                                                                            sticky=W + E + N + S, padx=10,
                                                                            pady=5)
            Label(separator, text=prod[3], background=red, width=10).grid(row=row, column=2,
                                                                            sticky=W + E + N + S, padx=10,
                                                                            pady=5)
        else:
            Label(separator, text=prod[1], background=color, width=10).grid(row=row, column=0,
                                                                            sticky=W + E + N + S, padx=10, pady=5)
            Label(separator, text=prod[2], background=color, width=10).grid(row=row, column=1,
                                                                            sticky=W + E + N + S, padx=10,
                                                                            pady=5)
            Label(separator, text=prod[3], background=color, width=10).grid(row=row, column=2,
                                                                            sticky=W + E + N + S, padx=10,
                                                                            pady=5)


        btn_a1 = Button(separator, text="Update", width=7, command=lambda prod=prod: updateProduct(prod[0]))
        btn_a2 = Button(separator, text="Delete", width=7, command=lambda prod=prod: deleteProduct(prod[0]))

        btn_a1.grid(row=row, column=3, sticky=W, padx=5, pady=5)
        btn_a2.grid(row=row, column=4, sticky=E, padx=5, pady=5)
        row += 1
        cursor.commit()

    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')


def addHeaders():
    separator.grid(row=5, column=0, columnspan=5, pady=5, sticky=W + E + N + S)
    Label(separator, text="Name", background=color, width=10).grid(row=0, column=0, sticky=W, padx=10, pady=5)
    Label(separator, text="Price", background=color, width=10).grid(row=0, column=1, sticky=W, padx=10, pady=5)
    Label(separator, text="Quantity", background=color, width=10).grid(row=0, column=2, sticky=W, padx=10, pady=5)
    Label(separator, text="Action", background=color, width=10).grid(row=0, column=3, sticky=W, padx=10, pady=5,
                                                                     columnspan=2)

root = Tk()
root.title("Simple Inventory System")
root.geometry("435x400")
root.resizable(0, 0)


Label(root, text="Products Information").grid(row=0, column=0, sticky=W, padx=10, pady=5)
Label(root, text="Product Name: ").grid(row=1, column=0, sticky=W, padx=10, pady=5)
Label(root, text="Product Price: ").grid(row=2, column=0, sticky=W, padx=10, pady=5)
Label(root, text="Product Quantity: ").grid(row=3, column=0, sticky=W, padx=10, pady=5)

e1 = Entry(root, width=45)
e2 = Entry(root, width=45)
e3 = Entry(root, width=45)

e1.grid(row=1, column=1, sticky=W, padx=10, pady=5, columnspan=2)
e2.grid(row=2, column=1, sticky=W, padx=10, pady=5, columnspan=2)
e3.grid(row=3, column=1, sticky=W, padx=10, pady=5, columnspan=2)

btn1 = Button(root, text="Update Product", width=15, state=DISABLED, background = gray)
btn2 = Button(root, text="Add Product", width=15, state=NORMAL, command=addProduct, background = light)
btn3 = Button(root, text="Cancel", width=15, state=DISABLED, command=cancelUpdate, background = gray)

btn1.grid(row=4, column=1, sticky=W, padx=10, pady=5)
btn2.grid(row=4, column=2, sticky=E, padx=10, pady=5)
btn3.grid(row=4, column=0, sticky=W, padx=10, pady=5)

separator = Canvas(root, height=100, width=420, background=color, relief=SUNKEN)

addHeaders()
viewProducts()
root.mainloop()