import Tkinter
import json
import random


def set_appearance(window):
    set_background_image_and_quote(window)


def set_background_image_and_quote(window):
    background_image = Tkinter.Image("photo", file='background.png')
    canvas = Tkinter.Canvas(window, width=800, height=650)
    canvas.create_image(0, 0, image=background_image, anchor="nw")
    with open('quotes.json') as f:
        lines = (l.strip() for l in f)
        quote_and_author = random.choice([json.loads(l.decode('utf-8')) for l in lines if l])
    quote = quote_and_author[0]
    author = "- " + quote_and_author[1]
    text = canvas.create_text(400, 225, fill="#fdf8f8", font="Halvetica 20", text=quote, width=550)
    x1, y1, x2, y2 = canvas.bbox(text)
    canvas.create_text(450, y2 + 30, fill="#cedcdf", font="Halvetica 20", text=author)
    canvas.pack(side="top", fill="both", expand=True)
    window.mainloop()