# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 23:08:44 2019

@author: Nikhil
"""

# import modules
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import mailsender as ms


'''
# Send mail function
def send_mail(gmail, to, password, message):
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(gmail,password)
    s.sendmail(gmail,to,message)
    
    s.quit()
'''
    
    
# Create window  
root = Tk()


# Create labels
useremail_label = ttk.Label(root, text='Enter your email :', font={'helvetica', 100})
useremail_label.grid(row=0, column=0, sticky=W)

userpassword_label = ttk.Label(root, text='Enter your password :', font={'helvetica', 100})
userpassword_label.grid(row=1, column=0, sticky=W)

receiveremail_label = ttk.Label(root, text='Enter receivers email :', font={'helvetica', 100})
receiveremail_label.grid(row=2, column=0, sticky=W)

message_label = ttk.Label(root, text='Enter message to be sent :', font={'helvetica', 100}, wraplength=100)
message_label.grid(row=3, column=0, columnspan=2, sticky=W)


# Create entry
email_var = StringVar()
user_email = ttk.Entry(root, textvariable=email_var, width=50)
user_email.grid(row=0, column=1)

password_var = StringVar()
user_password = ttk.Entry(root, textvariable=password_var, width=50)
user_password.grid(row=1, column=1)

receiver_var = StringVar()
receiver_email = ttk.Entry(root, textvariable=receiver_var, width=50)
receiver_email.grid(row=2, column=1)

message_var = StringVar()
message_entry = ttk.Entry(root, textvariable=message_var, width=50)
message_entry.grid(row=3, column=1)


# Button click event function
def btn_click():
    
    email = str(email_var.get())
    password = str(password_var.get())
    receiver = str(receiver_var.get())
    message = str(message_var.get())
    
#    file = filedialog.askopenfilename()
    send_mail(email,receiver,password,message)
    
    display_label = ttk.Label(root, text = 'Message sent!', font={'comic-sans', 100})
    display_label.grid(row=5, column=0, columnspan=2, sticky=W)
    


# Create button
btn = Button(root, text='Send', command=btn_click)
btn.grid(row=4, column=1)




root.mainloop()