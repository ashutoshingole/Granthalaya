import Tkinter
import dimensions
import validations
import errors
import constants
import apis
import mysqldb
from ScrolledText import *


# _Author_ = 'Ashutosh Ingole'

def on_select(evt):
    value = str(bookList.get(bookList.curselection()))
    bookInfo.config(state='normal')
    bookInfo.delete('1.0', 'end')
    bookInfo.insert('end', "Title\t" + " : " + str(my_dict[value][0]))
    bookInfo.insert('end', '\n')
    bookInfo.insert('end', "Author\t" + " : " + str(my_dict[value][1]))
    bookInfo.insert('end', '\n')
    bookInfo.insert('end', "Genre\t" + " : " + str(my_dict[value][2]))
    bookInfo.insert('end', '\n')
    bookInfo.insert('end', "Rating\t" + " : " + str(my_dict[value][3]))
    bookInfo.insert('end', '\n')
    bookInfo.insert('end', "ISBN\t" + " : " + str(my_dict[value][4]))
    bookInfo.insert('end', '\n')
    bookInfo.insert('end', "Price\t" + " : " + str(my_dict[value][5]))
    bookInfo.insert('end', '\n')
    bookInfo.insert('end', "\n\t" + str(my_dict[value][6]))
    bookInfo.config(state='disabled')


def validate(entry_info):
    condition_2 = validations.validate_alpha_only_string(entry_info[1].get())
    condition_3 = validations.validate_num_only_string(entry_info[2].get())
    condition_4 = validations.validate_num_only_string(entry_info[3].get())

    if not (condition_2 and condition_3 and condition_4):
        if not condition_2:
            return 2
        if not condition_3:
            return 3
        if not condition_4:
            return 4
    else:
        return 0


def destroy_add_book_window(window):
    window.destroy()


def add_to_db(entry_info, window):
    validation_response = validate(entry_info)
    if validation_response != 0:
        errors.map_error(validation_response)
    else:
        book_info = []
        for item in entry_info:
            book_info.append(item.get())
        ans_1 = mysqldb.check_if_book_exist(book_info[0])
        if ans_1 != 0:
            errors.raise_book_exist_error()
        else:
            isbn = book_info[2]
            response = apis.get_book_rating_and_info_and_genre(isbn)
            book_info.append(response[0])
            book_info.append(response[1])
            book_info.append(response[2])
            ans = mysqldb.check_if_author_exist(book_info[1])
            if ans == 0:
                author_id = response[3]
                author_name = book_info[1]
                image_url = response[4]
                author_info = apis.get_author_info_and_image(author_id, author_name, image_url)
                mysqldb.add_author_info_to_db(author_name, author_info)

            mysqldb.add_new_book_entry_to_db(book_info)

    destroy_add_book_window(window)
    return


def get_book_entry_details():
    window = Tkinter.Toplevel()
    window.wm_title("Add New Book")
    dimensions.set_dimensions(window)
    background_image = Tkinter.Image("photo", file='background.png')
    canvas = Tkinter.Canvas(window, width=constants.window_width, height=constants.window_height)
    canvas.create_image(0, 0, image=background_image, anchor="nw")

    title_entry = Tkinter.Entry(canvas, width=40)
    author_entry = Tkinter.Entry(canvas, width=40)
    isbn_entry = Tkinter.Entry(canvas, width=40)
    price_entry = Tkinter.Entry(canvas, width=40)

    canvas.create_window(500, 100, window=title_entry)
    canvas.create_window(500, 150, window=author_entry)
    canvas.create_window(500, 200, window=isbn_entry)
    canvas.create_window(500, 250, window=price_entry)

    canvas.create_text(255, 100, fill="#fdf8f8", font="Halvetica 14", text="Book Title :")
    canvas.create_text(240, 150, fill="#fdf8f8", font="Halvetica 14", text="Author Name :")
    canvas.create_text(280, 200, fill="#fdf8f8", font="Halvetica 14", text="ISBN :")
    canvas.create_text(280, 250, fill="#fdf8f8", font="Halvetica 14", text="Price :")

    entry_info = [title_entry, author_entry, isbn_entry, price_entry]

    add_button = Tkinter.Button(window, text="Add", command=lambda: add_to_db(entry_info, window))
    canvas.create_window(450, 350, anchor=Tkinter.NW, window=add_button)

    cancel_button = Tkinter.Button(window, text="Cancel", command=lambda: destroy_add_book_window(window))
    canvas.create_window(550, 350, anchor=Tkinter.NW, window=cancel_button)
    canvas.pack(side="top", fill="both", expand=True)
    canvas.update()
    window.mainloop()


def get_all_books():
    window = Tkinter.Toplevel()
    window.configure(bg='lightgrey')
    window.title("All Books From Library")
    dimensions.set_dimensions(window)
    cursor = mysqldb.get_all_books_from_db()
    global my_dict
    my_dict = {}
    for item in cursor:
        my_dict[item[0]] = [item[0], item[1], item[2], item[3], item[4], item[5], item[6]]

    lbl1 = Tkinter.Label(window, text="Books List:", fg='black', font=("Helvetica", 16, "bold"))
    lbl2 = Tkinter.Label(window, text="Book Information:", fg='black', font=("Helvetica", 16, "bold"))
    lbl1.grid(row=0, column=0, sticky='W')
    lbl2.grid(row=0, column=1, sticky='W')

    frm = Tkinter.Frame(window)
    frm.grid(row=1, column=0, sticky='N' + 'S')
    window.rowconfigure(1, weight=1)
    window.columnconfigure(1, weight=1)

    scrollbar = Tkinter.Scrollbar(frm, orient="vertical")
    scrollbar.pack(side='right', fill='y')

    global bookList

    bookList = Tkinter.Listbox(frm, width=20, yscrollcommand=scrollbar.set, font=("Helvetica", 12),
                               selectmode='single')
    bookList.pack(expand=True, fill='y')
    scrollbar.config(command=bookList.yview)

    global bookInfo

    bookInfo = ScrolledText(window, height=25, wrap='word', font=("Helvetica", 12))
    bookInfo.grid(row=1, column=1, sticky='E' + 'W' + 'N')
    for item in cursor:
        bookList.insert('end', item[0])

    bookList.bind('<<ListboxSelect>>', on_select)
    window.mainloop()
