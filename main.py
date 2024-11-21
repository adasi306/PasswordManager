from tkinter import *
from tkinter import messagebox, simpledialog
import random
import json
import string
import base64
import hashlib
from cryptography.fernet import Fernet

letters: list[str] = list(string.ascii_letters)
numbers: list[str] = list(string.digits)
symbols: list[str] = ["!", "%", "$", "&", "^"]


def generate_key(master_password: str) -> bytes:
    master_password = master_password.encode()
    key = hashlib.sha256(master_password).digest()
    key = base64.urlsafe_b64encode(key)
    return key


def generate_password() -> None:

    def random_letter() -> str:
        return random.choice(letters)

    def random_symbol() -> str:
        return random.choice(symbols)

    def random_number() -> str:
        return random.choice(numbers)

    password_input.delete(0, "end")

    elements: list[str] = (
        [random_letter() for _ in range(random.randint(8, 10))]
        + [random_symbol() for _ in range(random.randint(2, 4))]
        + [random_number() for _ in range(random.randint(2, 4))]
    )
    random.shuffle(elements)
    password: str = "".join(elements)
    password_input.insert(0, password)


def save_password() -> None:
    website: str = web_input.get()
    username: str = username_input.get()
    password: str = password_input.get()

    if website == "" or username == "" or password == "":
        messagebox.showinfo(
            title="Error", message="Please don't leave any fields empty"
        )
        return

    master_password: str | None = simpledialog.askstring(
        "Master Password", "Enter your master password:", show="*"
    )
    if not master_password:
        messagebox.showinfo(title="Error", message="Master password is required.")
        return

    key: bytes = generate_key(master_password)
    fernet: Fernet = Fernet(key)
    encrypted_password: str = fernet.encrypt(password.encode()).decode()

    new_data: dict[str, dict[str, str]] = {
        website: {
            "email/username": username,
            "password": encrypted_password,
        }
    }

    try:
        with open("portfolio/passwordmanager/data.json", "r") as data_file:
            try:
                data: dict[str, dict[str, str]] = json.load(data_file)
            except json.decoder.JSONDecodeError:
                data = {}
    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open("portfolio/passwordmanager/data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    web_input.delete(0, END)
    username_input.delete(0, END)
    password_input.delete(0, END)


def find_password() -> None:
    website: str = web_input.get()

    try:
        with open("portfolio/passwordmanager/data.json") as data_file:
            data: dict[str, dict[str, str]] = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
        return

    if website in data:
        master_password: str | None = simpledialog.askstring(
            "Master Password", "Enter your master password:", show="*"
        )
        if not master_password:
            messagebox.showinfo(title="Error", message="Master password is required.")
            return

        key: bytes = generate_key(master_password)
        fernet: Fernet = Fernet(key)

        email: str = data[website]["email/username"]
        encrypted_password: str = data[website]["password"]

        try:
            decrypted_password: str = fernet.decrypt(encrypted_password.encode()).decode()
        except Exception:
            messagebox.showinfo(title="Error", message="Incorrect master password.")
            return

        messagebox.showinfo(
            title=website,
            message=f"Email/Username: {email} \nPassword: {decrypted_password}",
        )
    else:
        messagebox.showinfo(title="Error", message="No details for the website exist")


window: Tk = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70, bg="white")

web_label: Label = Label(text="Website:")
web_label.grid(column=0, row=1)

web_input: Entry = Entry(width=35)
web_input.grid(column=1, row=1)
web_input.focus()

username_label: Label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_input: Entry = Entry(width=35)
username_input.grid(column=1, row=2)

password_label: Label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input: Entry = Entry(width=35)
password_input.grid(column=1, row=3)

gen_button: Button = Button(text="Generate Password", command=generate_password)
gen_button.grid(column=2, row=3)

add_button: Button = Button(text="Add", width=29, command=save_password)
add_button.grid(column=1, row=4)

search_button: Button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)

canvas: Canvas = Canvas(width=200, height=200)
try:
    logo_img: PhotoImage = PhotoImage(file="portfolio/passwordmanager/logo.png")
    canvas.create_image(100, 100, image=logo_img)
except Exception as e:
    messagebox.showinfo(title="Error", message=f"Logo image not found: {e}")
canvas.grid(column=1, row=0)

window.mainloop()
