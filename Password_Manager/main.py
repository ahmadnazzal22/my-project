from tkinter import *
from tkinter import messagebox
import random
import json

# --- 1. توليد كلمة المرور (Password Generator) ---
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = [random.choice(letters) for _ in range(8)]
    password_symbols = [random.choice(symbols) for _ in range(2)]
    password_numbers = [random.choice(numbers) for _ in range(2)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# --- 2. حفظ البيانات (Save Data) ---
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = new_data
        else:
            data.update(new_data)

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
            
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo(title="Success", message="Data saved successfully!")

# --- 3. إعداد الواجهة (UI Setup) ---
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
# ملاحظة: يمكنك إضافة صورة شعار (logo.png) هنا إذا أردت
# logo_img = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# العناوين (Labels)
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# خانات الإدخال (Entries)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ahmad@example.com") # إيميل افتراضي
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# الأزرار (Buttons)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()