from tkinter import *
import pyshorteners
import pyperclip


root = Tk()
root.geometry("376x268")
root.title("URL Shortener")
root.configure(bg="#3a3836")
url = StringVar()
url_address = StringVar()


def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)


def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)


Label(root, text="🐍 URL Shortener", font=["Helvetica", 17]).pack(pady=10)
Label(root, text="Enter your URL", font=["Helvetica", 15]).pack(pady=15)
Entry(root, textvariable=url, font=["Helvetica", 13]).pack(pady=2)
Button(root, text="Generate Short URL", command=urlshortener).pack(pady=12)
Entry(root, textvariable=url_address, font=["Helvetica", 13]).pack(pady=7)
Button(root, text="Copy Short URL", command=copyurl).pack(pady=7)

root.mainloop()