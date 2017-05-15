import Tkinter
import dimensions
import validations
import errors
import constants


def validate(entry_info):
    condition_1 = validations.validate_alpha_only_string(entry_info[0])
    condition_2 = validations.validate_alpha_only_string(entry_info[1])
    condition_3 = validations.validate_num_only_string(entry_info[2])
    condition_4 = validations.validate_num_only_string(entry_info[3])

    if not (condition_1 and condition_2 and condition_3 and condition_4):
        print


def destroy_add_book_window(window):
    window.destroy()


def add_to_db(entry_info, window):
    if validate(entry_info):
        print
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
    return