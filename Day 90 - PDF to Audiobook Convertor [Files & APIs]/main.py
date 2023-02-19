import PyPDF2
from gtts import gTTS

language = 'en'

pdfFile = open('pdfs/test.pdf', 'rb')

pdfFileReader = PyPDF2.PdfReader(pdfFile)

pages = len(pdfFileReader.pages)
text_list = []

for page_num in range(pages):
    try:
        page = pdfFileReader.pages[0]
        text_list.append(page.extract_text())
    except:
       pass

text = " ".join(text_list)

audio = gTTS(text=text, lang=language, slow=False)
audio.save("audios/<name>.mp3")

pdfFile.close()
