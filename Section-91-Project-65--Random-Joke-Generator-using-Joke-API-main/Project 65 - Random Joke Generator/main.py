from tkinter import *
import requests


def get_joke():
    response = requests.get("http://official-joke-api.appspot.com/random_joke")
    response.raise_for_status()
    data = response.json()
    setup = data["setup"]
    punchline = data["punchline"]
    quote = f"{setup}\n\n{punchline}"
    canvas.itemconfig(quote_text, text=quote)

window = Tk()
window.title("Random Jokes..")
window.config(padx=50, pady=50)

canvas = Canvas(width=400, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(300, 300, image=background_img)
quote_text = canvas.create_text(150, 207, text="I know a joke, but it is not funny", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)


joke_button = Button(text ="Get Random Joke", highlightthickness=1, command=get_joke)
joke_button.grid(row=1, column=0)



window.mainloop()