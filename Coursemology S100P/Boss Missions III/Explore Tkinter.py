import tkinter as tk
from tkinter import messagebox

def submit():
    username = form_username.get()
    email = form_email.get()
    password = form_password.get()
    phone_number = form_phone.get()

    message = f"Username: {username} \nEmail: {email} \nPassword: {password} \nPhone Number: {phone_number}"
    messagebox.showinfo("Registration Details", message)

root = tk.Tk()
root.title("Register Form")
root.configure(bg='#F0F0F0')

label_username = tk.Label(root, text="Username:", bg='#F0F0F0')
label_email = tk.Label(root, text="Email:", bg='#F0F0F0')
label_password = tk.Label(root, text="Password:", bg='#F0F0F0')
label_phone = tk.Label(root, text="Phone Number:", bg='#F0F0F0')

form_username = tk.Entry(root, bg='#D3D3D3', fg='#000000')
form_email = tk.Entry(root, bg='#D3D3D3', fg='#000000')
form_password = tk.Entry(root, show="*", bg='#D3D3D3', fg='#000000')
form_phone = tk.Entry(root, bg='#D3D3D3', fg='#000000')

submit_button = tk.Button(root, text="Submit", command=submit, bg='#4CAF50', fg='#FFFFFF')

label_username.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
form_username.grid(row=0, column=1, padx=10, pady=5)

label_email.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
form_email.grid(row=1, column=1, padx=10, pady=5)

label_password.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
form_password.grid(row=2, column=1, padx=10, pady=5)

label_phone.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
form_phone.grid(row=3, column=1, padx=10, pady=5)

submit_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()