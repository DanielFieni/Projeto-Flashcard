from tkinter import *
import pandas   
from random import choice
random_word = {}

BACKGROUND_COLOR = "#B1DDC6"

# ================== READ DATA ================== #
try:
    data = pandas.read_csv("data/english_words_to_learn.csv")
except:
    new_data = pandas.read_csv("data/english_words.csv")
    learn = new_data.to_dict(orient="records")
else:
    learn = data.to_dict(orient="records")


# ================== CHANGE WORD ================== #
def change_word():
    global random_word, flip_card
    window.after_cancel(flip_card)
    random_word = choice(learn)
    canvas.itemconfig(card_language, text="English", fill="black")
    canvas.itemconfig(card_word, text=random_word["English"], fill="black")
    canvas.itemconfig(image_front, image=card_front)
    flip_card = window.after(3000, func=change_background)

# ================== CHANGE BACKGROUND ================== #
def change_background():
    canvas.itemconfig(card_language, text="Português", fill="white")
    canvas.itemconfig(card_word, text=random_word["Portuguese"], fill="white")
    canvas.itemconfig(image_front, image=card_back)

# ================== ANSWER CORRECT ================== #
def correct():
    learn.remove(random_word)
    data_update = pandas.DataFrame(learn)
    data_update.to_csv("data/english_words_to_learn.csv", index=False)
    change_word()

# ================== LAYOUT ================== #
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_card = window.after(3000, func=change_background)

# CREATE FRONT IMAGE
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file="images/card_front.png")
image_front = canvas.create_image(400, 263, image=card_front)

card_back = PhotoImage(file="images/card_back.png")

canvas.grid(column=0, row=0, columnspan=2)
card_language = canvas.create_text(400, 150, text="card_language", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, command=change_word)
button_wrong.grid(column=0, row=1)

image_right = PhotoImage(file="images/right.png")
button_right = Button(image=image_right, highlightthickness=0, command=correct)
button_right.grid(column=1, row=1)

change_word()

window.mainloop()