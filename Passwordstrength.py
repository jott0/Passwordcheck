import tkinter as tk
from tkinter import messagebox

def checkPassword(password):
    upperChars, lowerChars, specialChars, digits, length = 0, 0, 0, 0, 0
    length = len(password)
    strength_message = ""
    spl_char = "!@#$%^&*()-+?_=,<>/"

    if length <= 6:
        strength_message += "Password must contain at least 6 characters!\n"

    for char in password:
        if char.isupper():
            upperChars += 1
        if char.islower():
            lowerChars += 1
        if char.isdigit():
            digits += 1
        if char in spl_char:
            specialChars += 1

    if upperChars != 0 and lowerChars != 0 and digits != 0 and specialChars != 0:
        if length >= 10:
            strength_message += "The strength of the password is strong.\n"

    if length >= 6 and length < 10:
        if upperChars != 0 or lowerChars != 0 or digits != 0 or specialChars != 0:
            strength_message += "The strength of the password is medium.\n"

    if length < 6:
        if upperChars != 0 or lowerChars != 0 or digits != 0 or specialChars != 0:
            strength_message += "The strength of the password is weak.\n"
    else:
        if upperChars == 0:
            strength_message += "Password must contain at least one uppercase character!\n"

        if lowerChars == 0:
            strength_message += "Password must contain at least one lowercase character!\n"

        if specialChars == 0:
            strength_message += "Password must contain at least one special character!\n"

        if digits == 0:
            strength_message += "Password must contain at least one digit!\n"

    return strength_message

def display_password_strength():
    password_strength = checkPassword(password_entry.get())
    messagebox.showinfo("Password Strength", password_strength)

root = tk.Tk()
root.geometry("300x200")
root.title("Password Strength Checker")

password_label = tk.Label(root, text="Enter Password:")
password_label.pack()

password_entry = tk.Entry(root, show="")
password_entry.pack()

check_button = tk.Button(root, text="Check Password Strength", command=display_password_strength)
check_button.pack()

root.mainloop()
