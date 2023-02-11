from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont
import uuid

_uuid = uuid.uuid4()

win = Tk()

win.geometry("700x550")
win.title("Image Watermarking - Upload Image and Add Your Watermark")
text_font = ('times', 18, 'bold')

l1 = Label(win, text="Upload Image", width=30, font=text_font)
l1.grid(row=1, column=1, padx=130, pady=30)
  
def make_label(parent, img):
    label = Label(parent, image=img)
    label.grid(row=4, column=1)
    
def upload_file():
    file_types = [ ('JPG Files', '*.jpg',),('PNG Files','*.png')]
    filename = filedialog.askopenfilename(filetypes=file_types, initialdir='/Users/USER/Downloads')
    if not filename:
        return

    img = Image.open(filename)
    imdraw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 40)
    imdraw.text((5, 5), "juba-portfolio.netlify.app", font=font, fill='#fff')
    
    # Save to local directory
    img.save(f"{_uuid}.png")
      
    img = img.resize((400,300))
    img = ImageTk.PhotoImage(img)
    img_l  = Label(win)
    img_l.grid(row=4, column=1, pady=20)
    img_l.image = img
    img_l['image'] = img 
    
    msg  = Label(win, fg='#3CB043', width=30, text="Your image has been saved successfully.", font=text_font)
    msg.grid(row=5, column=1)

upload_btn = Button(text="Upload", bg="white", width=15, command=upload_file)
upload_btn.grid(row=3, column=1)

win.mainloop()