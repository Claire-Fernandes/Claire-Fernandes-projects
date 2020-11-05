from tkinter import *
#imorpting tkinter for GUI
def register():#Creating A function
    #Creating global variables
    global username
    global password
    global username_entry
    global password_entry
    global register_screen
    register_screen=Toplevel(main_screen)#Create a second window under the main window
    register_screen.geometry("300x250")#Setting the size of the second screen
    register_screen.title("Registration")#Creating the title of the Registration Window
    #Setting the text Variables
    username=StringVar()
    password=StringVar()
    #Set label user instruction
    Label(register_screen,text="Please enter all the details below",bg="orange").pack()
    Label(register_screen,text="")
    #Seting user name label
    username_label=Label(register_screen,text="Username *")
    username_label.pack()
    #setting username entry
    username_entry=Entry(register_screen,textvariable=username)
    username_entry.pack()
    # Seting password label
    password_label=Label(register_screen, text="Password *")
    password_label.pack()
    # setting password entry
    password_entry= Entry(register_screen, textvariable=password,show="*")
    password_entry.pack()
    Label(register_screen,text="").pack()
    #Creating a button
    Button(register_screen,text="Register",width=10,height=1,bg="orange",command=register_user).pack()
def login():
    global login_screen
    login_screen=Toplevel(main_screen)
    login_screen.title("Login Page")
    login_screen.geometry("300x250")
    Label(login_screen,text="Please enter details below:",bg="yellow").pack()
    Label(login_screen,text="").pack()
    global username_varify
    global password_varify
    username_varify=StringVar()
    password_varify=StringVar()
    global username_login_entry
    global password_login_entry
    Label(login_screen,text="Username *").pack()
    username_login_entry=Entry(login_screen,textvariable=username_varify)
    username_login_entry.pack()
    Label(login_screen,text="").pack()
    Label(login_screen,text="Password *").pack()
    password_login_entry=Entry(login_screen,textvariable=password_varify,show="*")
    password_login_entry.pack()
    Label(login_screen,text="").pack()
    Button(login_screen,text="Login",width=10,height=1,bg="yellow",command=login_varify).pack()
def register_user():
    #Getting username and password
    username_info=username.get()
    password_info=password.get()
    #opening a file in write mode.
    file=open(username_info,"w")
    #write the user name and password into the file.
    file.write(username_info + "\n")
    file.write(password_info)
    #closing the file
    file.close()
    #Deleting the entry
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    #Creating label
    Label(register_screen,text="Registration Sucsessfull",font=("Calibri",12),fg="green").pack()
def login_varify():
    username1=username_varify.get()
    password1=password_varify.get()
    username_login_entry.delete(0,END)
    password_login_entry.delete(0,END)
    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1=open(username1,"r")
        varify=file1.read().splitlines()
        if password1 in varify:
            login_sucsess()
        else:
            password_not_recognised()
    else:
        user_not_found()
def login_sucsess():
    global login_sucsess_screen
    login_sucsess_screen=Toplevel(login_screen)
    login_sucsess_screen.title("Success")
    login_sucsess_screen.geometry("150x100")
    Label(login_sucsess_screen,text="Login is sucsessful",fg="green").pack()
    Button(login_sucsess_screen,text="Ok",command=delete_login_success).pack()
def password_not_recognised():
    global password_screen
    password_screen=Toplevel(login_screen)
    password_screen.title("Success")
    password_screen.geometry("150x100")
    Label(password_screen,text="Invalid password",fg="red").pack()
    Button(password_screen,text="Ok",command=delete_password_screen).pack()
def user_not_found():
    global user_screen
    user_screen=Toplevel(login_screen)
    user_screen.title("Success")
    user_screen.geometry("150x100")
    Label(user_screen,text="Username not found",fg="red").pack()
    Button(user_screen,text="Ok",command=delete_user_screen).pack()
def delete_login_success():
    login_sucsess_screen.destroy()
def delete_password_screen():
    password_screen.destroy()
def delete_user_screen():
    user_screen.destroy()
def main_account_screen():#Creating A function
    global main_screen
    main_screen=Tk()#Creating a GUI window
    main_screen.geometry("300x250")#Setting the size of the main window
    main_screen.title("Account Login")#Creating the title of the main window
    Label(text="Choose Login or Register.",bg="blue",width=30,height=2,font=("Arial",15)).pack()#Creating a label to desplay the
    # text
    Label(text="").pack()#Creating a Label to creat the space between the buttons
    Button(text="Login",width=30,height=2,command=login).pack()#Creating a button
    Label(text="").pack()#Creating a Label to creat the space between the buttons
    Button(text="Register", width=30, height=2,command=register).pack()#Creating a button
    main_screen.mainloop()
main_account_screen()#Calling the function made