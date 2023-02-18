from tkinter import *

root = Tk()
root.geometry("700x500")
root.title("Disappearing Text Writing App")
text_font = ('Helvetica', 14, 'normal')
job_id = None

def handle_wait(event):
    global job_id

    if job_id is not None:
        root.after_cancel(job_id)

    job_id = root.after(5000, cls)

def cls():
    box.delete('1.0', END)

box = Text(font=text_font, bg="#000", fg="#0f0", highlightthickness=0)
box.bind('<Key>', handle_wait)
box.focus()
box.pack()

cls()
root.mainloop()