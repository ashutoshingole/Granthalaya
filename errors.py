from Tkinter import *
import tkMessageBox


def map_error(error_code):
    if error_code == 2:
        raise_author_error()
    elif error_code == 3:
        raise_isbn_error()
    else:
        raise_price_error()



def raise_author_error():
    tkMessageBox.showerror("Error", "Author name is incorrect")


def raise_isbn_error():
    tkMessageBox.showerror("Error", "ISBN is incorrect")


def raise_price_error():
    tkMessageBox.showerror("Error", "Price is incorrect")
