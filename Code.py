import tkinter as tk
import mysql.connector
import random

def userid():
    a=random.randint(1,9)
    b=random.randint(1,9)
    c=random.randint(1,9)
    d=random.randint(1,9)
    num="HDFC"+str(a)+str(b)+str(c)+str(d)
    return num

def uidcheck(USERID):
    con = mysql.connector.connect(host='localhost', database='octanet', user='root', password='')
    if con.is_connected():
        qry = "select USERID from atm_interface where USERID ='{}'".format(USERID)
        c1 = con.cursor()
        c1.execute(qry)
        rows = c1.fetchall()
        if c1.rowcount>0:
            x=True
        else:
            x=False
        return x

def pincheck(Pin):
    con = mysql.connector.connect(host='localhost', database='octanet', user='root', password='')
    if con.is_connected():
        qry = "select Pin from atm_interface where Pin ='{}'".format(Pin)
        c1 = con.cursor()
        c1.execute(qry)
        rows = c1.fetchall()
        if c1.rowcount>0:
            x=True
        else:
            x=False
        return x

class MainMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="HDFC Bank",padx=335,pady=46, fg='black', bg='#00FF00',font=('arial',25))
        self.label1.pack(pady=1.5)
        self.sign_in_button = tk.Button(self, text='Registration', command=self.Sign_in, padx=62, pady=18,bg='#FF3333', font=('arial', 15))
        self.sign_in_button.pack(pady=1.5)
        self.log_in_button = tk.Button(self, text='LOG IN', command=self.Log_in, padx=80, pady=18, bg='#FF3333',font=('arial', 15))
        self.log_in_button.pack(pady=1.5)
        self.quit_button = tk.Button(self, text="Quit", command=self.master.quit)
        self.quit_button.pack(pady=5)

    def Sign_in(self):
        self.master.switch_frame(Sign_in)

    def Log_in(self):
        self.master.switch_frame(Log_in)

class Sign_in(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="Welcome To HDFC Bank",padx=235,pady=47, fg='black', bg='#00FF00',font=('arial',25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="New Registration", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.Name_label = tk.Label(self, text="Enter Your Name:")
        self.Name_label.pack()
        self.Name_entry = tk.Entry(self)
        self.Name_entry.pack(pady=5)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.dob_label = tk.Label(self, text="Enter Your DOB:")
        self.dob_label.pack()
        self.dob_entry = tk.Entry(self)
        self.dob_entry.pack(pady=5)
        self.pin_label = tk.Label(self, text="Enter Your 6 Digit PIN:")
        self.pin_label.pack()
        self.pin_entry = tk.Entry(self)
        self.pin_entry.pack(pady=5)
        self.Reg_button = tk.Button(self, text='Register', command=self.Rega,font=('arial', 15))
        self.Reg_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(MainMenu)

    def Rega(self):
        con = mysql.connector.connect(host='localhost', database='octanet', user='root', password='')
        if con.is_connected():
            USERID = userid()
            Name = self.Name_entry.get()
            Email = self.email_entry.get()
            DOB = self.dob_entry.get()
            Pin = self.pin_entry.get()
            Money = 0
            qry = "insert into atm_interface values ('{}','{}','{}','{}',{},{})".format(USERID ,Name, Email,DOB,Pin,Money)
            c1 = con.cursor()
            c1.execute(qry)
            con.commit()
            con.close
            self.label1 = tk.Label(self, text="Thanks For Choosing HDFC bank \n"
                                              f"Your Userid : {USERID}", font=("Arial", 10))
            self.label1.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error(MySQL is not Connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close

class Log_in(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="Welcome To HDFC Bank", padx=235, pady=45, fg='black', bg='#00FF00',font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Log in Page", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.uid_label = tk.Label(self, text="Enter Your User_ID:")
        self.uid_label.pack()
        self.uid_entry = tk.Entry(self)
        self.uid_entry.pack(pady=5)
        self.pin_label = tk.Label(self, text="Enter Your 6 Digit Pin:")
        self.pin_label.pack()
        self.pin_entry = tk.Entry(self)
        self.pin_entry.pack(pady=5)
        self.log_in_button = tk.Button(self, text='Log in', command=self.search, font=('arial', 15))
        self.log_in_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(MainMenu)

    def search(self):
        con = mysql.connector.connect(host='localhost', database='octanet', user='root', password='')
        if con.is_connected():
            USERID = self.uid_entry.get()
            Pin = self.pin_entry.get()
            if uidcheck(USERID):
                if pincheck(Pin):
                    self.master.switch_frame(Customer)
                else:
                    self.label = tk.Label(self, text="Incorrect Pin", font=("Arial", 10))
                    self.label.pack(pady=5)
            else:
                self.label = tk.Label(self, text="Incorrect UserId", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

class Customer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="Welcome To HDFC Bank", padx=235, pady=35, fg='black', bg='#00FF00',font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.tra_his_button = tk.Button(self, text='Transaction History', command=self.Tran_His, padx=50, pady=15, bg='#FF3333',font=('arial', 15))
        self.tra_his_button.pack(pady=1.5)
        self.With_mon_button = tk.Button(self, text='Withdraw Money', command=self.withdraw, padx=60, pady=15, bg='#FF3333',font=('arial', 15))
        self.With_mon_button.pack(pady=1.5)
        self.Dep_mon_button = tk.Button(self, text='Deposit Money', command=self.deposit, padx=68, pady=15, bg='#FF3333', font=('arial', 15))
        self.Dep_mon_button.pack(pady=1.5)
        self.tra_mon_button = tk.Button(self, text='Transfer Money', command=self.transfer, padx=65, pady=15, bg='#FF3333', font=('arial', 15))
        self.tra_mon_button.pack(pady=1.5)
        self.clo_acc_button = tk.Button(self, text='Close Account', command=self.close, padx=71, pady=15, bg='#FF3333', font=('arial', 15))
        self.clo_acc_button.pack(pady=1.5)
        self.log_out_button = tk.Button(self, text="Log_out", command=self.go_to_main_menu)
        self.log_out_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(MainMenu)

    def Tran_His(self):
        self.master.switch_frame(Trans_money)

    def withdraw(self):
        self.master.switch_frame(With_money)

    def deposit(self):
        self.master.switch_frame(Dep_money)

    def transfer(self):
        self.master.switch_frame(Tra_money)

    def close(self):
        self.master.switch_frame(Close)

class Trans_money(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="Welcome To HDFC Bank", padx=235, pady=35, fg='black', bg='#00FF00',font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.uid_label = tk.Label(self, text="Enter Your User_ID:")
        self.uid_label.pack()
        self.uid_entry = tk.Entry(self)
        self.uid_entry.pack(pady=5)
        self.search_button = tk.Button(self, text='Search', command='#', font=('arial', 15))
        self.search_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(Customer)

class With_money(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="Welcome To HDFC Bank", padx=235, pady=35, fg='black', bg='#00FF00',font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.uid_label = tk.Label(self, text="Enter Your User_ID:")
        self.uid_label.pack()
        self.uid_entry = tk.Entry(self)
        self.uid_entry.pack(pady=5)
        self.search_button = tk.Button(self, text='Search', command=self.search1, font=('arial', 15))
        self.search_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(Customer)

    def search1(self):
        con = mysql.connector.connect(host='localhost', database='octanet', user='root', password='')
        if con.is_connected():
            USERID = self.uid_entry.get()
            if uidcheck(USERID):
                self.with_mon_label = tk.Label(self, text="Enter Money Which we want to Withdraw:")
                self.with_mon_label.pack()
                self.with_mon_entry = tk.Entry(self)
                self.with_mon_entry.pack(pady=5)
                self.add_button = tk.Button(self, text='Add_Money', command=self.add, font=('arial', 15))
                self.add_button.pack(pady=1.5)
            else:
                self.label = tk.Label(self, text="Incorrect UserId", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def add(self):
        con = mysql.connector.connect(host='localhost', database='octanet', user='root', password='')
        if con.is_connected():
            USERID = self.uid_entry.get()
            Money = self.with_mon_entry.get()
            qry = "update atm_interface set Money=Money-{} where USERID='{}'".format(Money, USERID)
            c1 = con.cursor()
            c1.execute(qry)
            con.commit()
            con.close
            self.label = tk.Label(self, text="Your Money has been Withdraw😊😊", font=("Arial", 10))
            self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

class Dep_money(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="Welcome To HDFC Bank", padx=235, pady=35, fg='black', bg='#00FF00',font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.uid_label = tk.Label(self, text="Enter Your User_ID:")
        self.uid_label.pack()
        self.uid_entry = tk.Entry(self)
        self.uid_entry.pack(pady=5)
        self.search_button = tk.Button(self, text='Search', command=self.search1, font=('arial', 15))
        self.search_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(Customer)

    def search1(self):
        con = mysql.connector.connect(host='localhost', database='octanet', user='root', password='')
        if con.is_connected():
            USERID = self.uid_entry.get()
            if uidcheck(USERID):
                self.dep_mon_label = tk.Label(self, text="Enter Money Which we want to Deposit:")
                self.dep_mon_label.pack()
                self.dep_mon_entry = tk.Entry(self)
                self.dep_mon_entry.pack(pady=5)
                self.add_button = tk.Button(self, text='Add_Money', command=self.add, font=('arial', 15))
                self.add_button.pack(pady=1.5)
            else:
                self.label = tk.Label(self, text="Incorrect UserId", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def add(self):
        con = mysql.connector.connect(host='localhost', database='octanet', user='root', password='')
        if con.is_connected():
            USERID = self.uid_entry.get()
            Money = self.dep_mon_entry.get()
            qry = "update atm_interface set Money=Money+{} where USERID='{}'".format(Money, USERID)
            c1 = con.cursor()
            c1.execute(qry)
            con.commit()
            con.close
            self.label = tk.Label(self, text="Your Money has been Deposit😊😊", font=("Arial", 10))
            self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

class Tra_money(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="Welcome To HDFC Bank", padx=235, pady=35, fg='black', bg='#00FF00',font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.uid1_label = tk.Label(self, text="Enter Sender User_ID:")
        self.uid1_label.pack()
        self.uid1_entry = tk.Entry(self)
        self.uid1_entry.pack(pady=5)
        self.search_button = tk.Button(self, text='Search', command=self.search1, font=('arial', 15))
        self.search_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(Customer)

    def search1(self):
        con = mysql.connector.connect(host='localhost', database='octanet', user='root', password='')
        if con.is_connected():
            USERID = self.uid1_entry.get()
            if uidcheck(USERID):
                self.uid2_label = tk.Label(self, text="Enter Receiver User_ID:")
                self.uid2_label.pack()
                self.uid2_entry = tk.Entry(self)
                self.uid2_entry.pack(pady=5)
                self.search_button = tk.Button(self, text='Search', command=self.search2, font=('arial', 15))
                self.search_button.pack(pady=1.5)
            else:
                self.label = tk.Label(self, text="Incorrect Sender UserId", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def search2(self):
        con = mysql.connector.connect(host='localhost', database='octanet', user='root', password='')
        if con.is_connected():
            USERID = self.uid2_entry.get()
            if uidcheck(USERID):
                self.tra_mon_label = tk.Label(self, text="Enter Money Which we want to Transfer:")
                self.tra_mon_label.pack()
                self.tra_mon_entry = tk.Entry(self)
                self.tra_mon_entry.pack(pady=5)
                self.add_button = tk.Button(self, text='Add_Money', command=self.add, font=('arial', 15))
                self.add_button.pack(pady=1.5)
            else:
                self.label = tk.Label(self, text="Incorrect Receiver UserId", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def add(self):
        con = mysql.connector.connect(host='localhost', database='octanet', user='root', password='')
        if con.is_connected():
            USERID1 = self.uid1_entry.get()
            USERID2 = self.uid2_entry.get()
            Money = self.tra_mon_entry.get()
            qry1 = "update atm_interface set Money=Money-{} where USERID='{}'".format(Money, USERID1)
            qry2 = "update atm_interface set Money=Money+{} where USERID='{}'".format(Money, USERID2)
            c1 = con.cursor()
            c1.execute(qry1)
            c1.execute(qry2)
            con.commit()
            con.close
            self.label = tk.Label(self, text="Your Money has been Transfer😊😊", font=("Arial", 10))
            self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

class Close(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="Welcome To HDFC Bank", padx=235, pady=35, fg='black', bg='#00FF00',font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.uid_label = tk.Label(self, text="Enter User_ID:")
        self.uid_label.pack()
        self.uid_entry = tk.Entry(self)
        self.uid_entry.pack(pady=5)
        self.delete_button = tk.Button(self, text='Delete', command=self.delete, font=('arial', 15))
        self.delete_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def delete(self):
        con = mysql.connector.connect(host='localhost', database='octanet', user='root', password='')
        if con.is_connected():
            USERID = self.uid_entry.get()
            if uidcheck(USERID):
                qry = "delete from atm_interface where USERID='{}'".format(USERID)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.label = tk.Label(self, text="Your Account Has Been Deleted😊😊\n"
                                                 "Thanks For Visiting HDFC Bank", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(MainMenu)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("E-learning Platform.")
        self.geometry("725x530")
        self.frames = {}
        for F in (MainMenu,Sign_in,Log_in,Customer,With_money,Dep_money,Tra_money,Close,Trans_money):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.switch_frame(MainMenu)

    def switch_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
