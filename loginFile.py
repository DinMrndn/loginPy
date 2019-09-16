from tkinter import *

class Users:
    def __init__(self,username, password):
        self.username = username
        self.password = password
    def Getusername(self):
        return self.username
    def Getpassword(self):
        return self.password

def wrongLogin():
    reg = Tk()
    reg.geometry("300x40+600+270")
    Label(reg, text="Your username/password is incorrect.", padx = 10, pady = 10).pack()

def reged():
    reg = Tk()
    reg.geometry("300x40+600+270")
    Label(reg, text="Your registration was successful!", padx=10, pady=10).pack()

def successfulLogin():
    reg = Tk()
    reg.geometry("300x40+600+270")
    Label(reg, text="You have successfully logged in!", padx=10, pady=10).pack()

def runLogin():
    username_info = Users.username.get()
    password_info = Users.password.get()
    number = 0
    if username_info == "" or password_info == "":
        ...
    else:
        while True:
            for running in open("Register.txt"):
                xsplit = running.strip('\n').split("??")
                if xsplit[0] == username_info and xsplit[1] == password_info:
                    number = 1
            if number == 1:
                successfulLogin()
            else:
                wrongLogin()
            break

def runRegister():
    username_info = Users.username.get()
    password_info= Users.password.get()
    if username_info == "" or password_info == "":
        ...
    else:
        reg = open("Register.txt","a")
        reg.write(username_info + "??" + password_info + "\n")
        reged()

def mainFrame():
    loginregister.destroy()
    global root
    root = Tk()
    root.geometry("200x170+600+270")
    root.title("Login System")
    root.resizable(0, 0)

    #global declarations
    global txtuser
    global txtpass

    #Initializations
    Users.username = StringVar()
    Users.password = StringVar()

    #FrameElements
    Label(root, text="Din's Login System", padx=5, pady=5, font="bold").grid(columnspan=2, row =0)
    Label(root, text="USERNAME:" ,padx=5, pady=5).grid(column=0, row =1)
    Label(root, text="PASSWORD:", padx=5, pady=5).grid(column=0, row =2)
    txtuser = Entry(root, textvariable=Users.username).grid(column=1, row =1)
    txtpass = Entry(root, textvariable=Users.password).grid(column=1, row =2)
    btnregister = Button(root,text= loreg, command = decider,padx=5, pady=5).grid(columnspan=2, row=3)
    back = Button(root, text="back", command=logregdestroyer, padx=5, pady=5).grid(columnspan=2, row=4)

def decider():
    if loreg == "Register":
        runRegister()
    elif loreg == "Login":
        runLogin()

def registerclick():
    global loreg
    loreg = "Register"
    mainFrame()

def loginclick():
    global loreg
    loreg = "Login"
    mainFrame()

def logregdestroyer():
    root.destroy()
    regorlog()

def regorlog():
    global loginregister
    global loreg
    loreg = str
    loginregister = Tk()
    loginregister.geometry("50x70+600+270")
    loginregister.title("Login System")
    btnregister = Button(loginregister,text= "REGISTER", command = registerclick,padx=5, pady=5, width="15").grid(row=0,sticky=N+S+W+E)
    btnlogin = Button(loginregister, text="LOGIN", command=loginclick, padx=5, pady=5).grid( row=1, sticky=N+S+W+E)
    loginregister.mainloop()

#run the first frame
regorlog()
