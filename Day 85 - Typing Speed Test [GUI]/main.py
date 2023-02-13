from tkinter import *
from threading import Thread
from time import sleep
from text import text, display_text

root = Tk()

root.geometry("1000x600")
root.title("Typing Speed Test ⌨️")

font = ('Helvetica', 14)
counter = 0
is_on = False

def time_threading():
    global is_on
    global counter
    
    while is_on:
        sleep(0.1)
        counter += 0.1
        wps = len(input_ent.get().split(" ")) / counter   # Words per second
        wpm = wps * 60                                    # Words per minute
        speed_l.config(text=f"Speed: \n{wps:.2f} WPS\n{wpm:.2f} WPM")

def start(event):
    global is_on

    if not is_on:
        if not event.keycode in [16, 17, 18]:      # shift, alt, ctrl
            is_on = True
            t = Thread(target=time_threading)
            t.setDaemon(True)
            t.start()
    if not text.startswith(input_ent.get()):
        input_ent.config(fg='red')
    else:
        input_ent.config(fg='green')
    if input_ent.get() == text:
        is_on = False        
        input_ent.config(fg='green')


def reset():
    global is_on
    global counter
    
    is_on = False
    counter = 0
    speed_l.config(text="Speed: \n0.00 WPS\n0.00 WPM")
    input_ent.delete(0, END)

frame = Frame(root)


text_l = Label(frame, text=display_text, width=100, height=8, borderwidth=1, relief="solid")
text_l.grid(row=0, column=0, columnspan=2, padx=100, pady=30)

input_ent = Entry(frame, width=60, font=font)
input_ent.grid(row=1, column=0, columnspan=2, padx=50, pady=50)
input_ent.bind("<KeyRelease>", start)

speed_l = Label(frame, text="Speed: \n0.00 WPS\n0.00 WPM", font=('Helvetica', 12))
speed_l.grid(row=2, column=0, columnspan=2, padx=50, pady=50)

reset_btn = Button(frame, text="Reset", command=reset, bg='#3CB043', fg='#fff')
reset_btn.grid(row=3, column=0, columnspan=2, padx=50, pady=50)

frame.pack(expand=True)

root.mainloop()