import tkinter as tk
import subprocess
from tkinter import messagebox
import mysql.connector as mqc
import db_queries as db
from PIL import ImageTk, Image
import demo


mydb=mqc.connect(
    host="localhost",
    user="root",
    password="1234")

class Sign_up:
    def __init__(self,root):
        # Create a new Tkinter self.window1
        self.window1 = root
        self.window1.geometry("500x400")
        self.window1.resizable(False , False)
        self.frame_1=tk.Frame(self.window1)
        #self.frame_1.pack()
        self.frame_2=tk.Frame(self.window1)
        self.frame_3=tk.Frame(self.window1 , width=400 , height=300 , bg="#bca9a9")
        self.frame_4=tk.Frame(self.window1 , width=400 , height=300 , bg="#bca9a9")
      

        #opening the backgoung image for main frame out of the function for organise window
        #opening the logo image
        img=Image.open('Images/login_page(1).jpg')
        #resizing the image
        re_img=img.resize((500 , 400))
        #create an obj of tkinter imageTk
        self.img_2= ImageTk.PhotoImage(re_img)
        #creating canvas for background image
        canvas1 =tk.Canvas(self.frame_1 , width=500 , height=400)
        canvas1.create_image(0,0, image=self.img_2 , anchor = 'nw')
        canvas1.pack()
        #creating canvas for background image
        canvas2 =tk.Canvas(self.frame_2 , width=500 , height=400)
        canvas2.create_image(0,0, image=self.img_2 , anchor = 'nw')
        canvas2.pack()
        
        

        #calling the login page function to open the login page by default
        self.Login_page()


    #submit button
    def submit_form(self):
        # Get form values
        name = self.name_entry.get()
        email = self.email_entry.get()
        password =self.password_entry.get()
        cpassword=self.cpassword_entry.get()
        if name:
            if email:
                if password:
                    if cpassword:
                        if password!=cpassword:
                            messagebox.showinfo("Error", "Password and confirm password does not match"\
                                            "Write the correct password")
                        else:
                            # Do something with the form data (e.g. save to a database)
                            db.traverse()
                            db.insert_info(name , email , password)
                            self.go_to_demo()
                    else:
                        messagebox.showinfo("Error", "Confirm the password")
                else:
                    messagebox.showinfo("Error", "Enter password")
            else:
                messagebox.showinfo("Error", "Enter email")
        else:
            messagebox.showinfo("Error", "Enter name")

        # Clear form fields
        #self.name_entry.delete(0, tk.END)
        #self.email_entry.delete(0, tk.END)
        #self.password_entry.delete(0, tk.END)
        #self.cpassword_entry.delete(0, tk.END)


     #function for Loginng in the application
    def Login(self):
        email=self.email_E.get()
        password=self.pass_E.get()
        if email:
            if password:
                db.traverse()
                i=db.check_info(email , password)
                if i==0:
                    messagebox.showinfo("Error" , "Email or password not found "\
                            "Try again with correct credentials")
                else:
                    self.go_to_demo()
            else:
                messagebox.showinfo("Error" , "Enter password")
        else:
            messagebox.showinfo("Error" , "Enter email")
        


    def go_to_demo(self):
        self.window1.destroy()
        subprocess.call(['python' , 'demo.py'] , creationflags=subprocess.CREATE_NO_WINDOW)


    def Exit(self):
        self.window1.destroy()

    def Back_login(self):
        self.frame_2.pack_forget()
        self.Login_page()

    def Back_signup(self):
        self.frame_1.pack_forget()
        self.signup_page()

    

    #login function for opening login window
    def Login_page(self):
        self.window1.title("Login page")
        self.frame_1.pack()

        

        #extra grey layer on top of image
        self.frame_3.place(in_=self.frame_1 , anchor='c' , relx=0.5 , rely=0.5  )
        
        #making new login components
        head_label = tk.Label(self.frame_3, text="Login form" ,font=("Roboto", 18, 'bold') , width=15  , bg="#bca9a9")
        head_label.place(x=80 , y=0)

        
        email_L= tk.Label(self.frame_3,text="Email" ,font=("Roboto", 12, 'bold'), width=10 ,bg="#bca9a9" )
        email_L.place(x=40 , y=55)
        self.email_E= tk.Entry(self.frame_3 , bg="#bcbea9")
        self.email_E.place(x=220 , y=55)

        pass_L= tk.Label(self.frame_3 , text="Password" ,font=("Roboto", 12, 'bold') , width=10 , bg="#bca9a9")
        pass_L.place(x=40 , y=115)
        self.pass_E=tk.Entry(self.frame_3 , show='*' , bg="#bcbea9")
        self.pass_E.place(x=220 , y=115)

        Signup_B=tk.Button(self.frame_3 , text="Sign up" ,font=("Roboto", 12, 'bold'), command=self.Back_signup , bg="#bca9a9")
        Signup_B.place(x=45 , y=200)

        Status=tk.Label(self.frame_3 , text="Not an existing user? then signup" , font=("Roboto", 8) , bg="#bca9a9" )
        Status.place(x=20 , y=170)

        Login_B=tk.Button(self.frame_3 , text="Login" , font=("Roboto", 12, 'bold') , command=self.Login , bg="#bca9a9")
        Login_B.place(x=250 , y=200)

      
    def signup_page(self):
        self.window1.title("Sign up page")
        self.frame_2.pack()

      

        self.frame_4.place(in_=self.frame_2 , anchor='c' , relx=0.5 , rely=0.5  )

        # Create form labels and fields
        head_label = tk.Label(self.frame_4, text="Sign up form" ,font=("Roboto", 14, 'bold') , width=20 , bg="#bca9a9")
        head_label.place(x=80 , y=0)
        
        name_label = tk.Label(self.frame_4, text="Name" ,font=("Roboto", 12, 'bold') , width=10 , bg="#bca9a9")
        name_label.place(x=40 , y=40)
        self.name_entry = tk.Entry(self.frame_4 , bg="#bcbea9")
        self.name_entry.place(x=200 , y=40)

        email_label = tk.Label(self.frame_4, text="Email" , font=("Roboto", 12, 'bold') , width=10 , bg="#bca9a9")
        email_label.place(x=40 , y=80)
        self.email_entry = tk.Entry(self.frame_4 , bg="#bcbea9")
        self.email_entry.place(x=200 , y=80)

        password_label = tk.Label(self.frame_4, text="Password" , font=("Roboto", 12, 'bold') , width=10 , bg="#bca9a9")
        password_label.place(x=40 , y=120)
        self.password_entry = tk.Entry(self.frame_4, show="*" , bg="#bcbea9")
        self.password_entry.place(x=200 , y=120)

        cpassword_label = tk.Label(self.frame_4, text="Confirm Password" , font=("Roboto", 12, 'bold') , width=15 , bg="#bca9a9")
        cpassword_label.place(x=40 , y=160)
        self.cpassword_entry = tk.Entry(self.frame_4, show="*" , bg="#bcbea9")
        self.cpassword_entry.place(x=200 , y=160)

        submit_button = tk.Button(self.frame_4, text="Submit", font=("Roboto", 12, 'bold') , width=10, bg="#bca9a9" , 
                                  command=self.submit_form)
        submit_button.place(x=50, y=240)

        exit_button = tk.Button(self.frame_4, text="Exit", font=("Roboto", 12, 'bold') ,width=10, bg="#bca9a9",
                                  command=self.Exit)
        exit_button.place(x=250 , y=240)

        back_button=tk.Button(self.frame_2 , text="\u2190" , font =("Roboto" , 8) , command=self.Back_login , bg="#d6927f")
        back_button.place(x=0 , y=0)

         


#the main function
if __name__=='__main__':
    root=tk.Tk()
    obj=Sign_up(root)
    root.mainloop()





