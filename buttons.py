import Tkinter
import actions


def add_menu(window):
    menu_bar = Tkinter.Menu(window)
    file_menu = Tkinter.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Add New Book", command=actions.get_book_entry_details)
    file_menu.add_command(label="View All Books", command=actions.get_all_books)
    menu_bar.add_cascade(label="File", menu=file_menu)
    exit_menu = Tkinter.Menu(menu_bar, tearoff=0)
    exit_menu.add_command(label="Good Bye", command=window.quit)
    menu_bar.add_cascade(label="Exit", menu=exit_menu)
    window.config(menu=menu_bar)