from tkinter import *
from tkinter import messagebox

class SignUp(Frame):
    pass

class Application(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        self.Creat_widgets()

    def Creat_widgets(self): # interface
        self.tl=t.title("CaVid-G4 App") # title
        self.frame=t.geometry("300x140+500+180")
        t.resizable(width=False, height=False)

        self.lb=Label(t,text="--Well com to CaVidG4--") # <h1> lable
        self.lb.pack()

        self.lb1 = Label(t,text="Sign in Account") # <h2> sublable
        self.lb1.pack()

        self.lb_acc=Label(t,text="account: ") # <p> account
        self.lb_acc.pack()
        self.lb_acc.place(x=20,y=50)

        self.en_acc=Entry(t) # Entry account
        self.en_acc.pack()
        self.en_acc.place(x=77,y=50)

        self.lb_pass=Label(t,text="password: ") # <p> password
        self.lb_pass.pack()
        self.lb_pass.place(x=20,y=76)

        self.en_pass = Entry(t,show="*")  # Entry password
        self.en_pass.pack()
        self.en_pass.place(x=77, y=76)

        self.bt_login=Button(t,text="Log in",font=(13),height=2,command=self.Call) ############################# Button Login
        self.bt_login.pack()
        self.bt_login.place(x=220,y=46)

        self.bt_signup = Button(t,text="Sign up",command=self.Creat_Sigup) ####################### Button Sign up
        self.bt_signup.pack()
        self.bt_signup.place(x=77, y=100)


        def Creat_Sigup(self):
        top=Toplevel(t)
        self.frame = top.geometry("300x140+500+180")
        top.resizable(width=False, height=False)

        self.lb = Label(top, text="Sign Up", font=("", 14)).pack()

        self.lb_acc = Label(top, text="account: ")  # <p> account
        self.lb_acc.pack()
        self.lb_acc.place(x=20, y=50)

        self.en_acc = Entry(top)  # Entry account
        self.en_acc.pack()
        self.en_acc.place(x=77, y=50)

        self.lb_pass = Label(top, text="password: ")  # <p> password
        self.lb_pass.pack()
        self.lb_pass.place(x=20, y=76)

        self.en_pass = Entry(top, show="*")  # Entry password
        self.en_pass.pack()
        self.en_pass.place(x=77, y=76)

        self.lb_conf = Label(top, text="confirm: ")  # <p> confirm
        self.lb_conf.pack()
        self.lb_conf.place(x=20, y=100)

        self.en_conf = Entry(top, show="*")  # Entry confirm
        self.en_conf.pack()
        self.en_conf.place(x=77, y=100)

        self.bt_login = Button(top, text="Submit", font=(13), height=2)  ############### Button Submit
        self.bt_login.pack()
        self.bt_login.place(x=220, y=70)
        
    def Call(self):



if __name__=="__main__":
    t=Tk()
    app=Application(t)
    app.mainloop()
