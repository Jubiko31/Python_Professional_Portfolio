from pytube import YouTube

def Download(url):
    yt = YouTube(url)
    yt = yt.streams.get_highest_resolution()
    try:
        yt.download()
    except:
        print("Uh...Something Went Wrong.")
    print("Video Downloaded Successfully ✔️")


url = input("Enter the YouTube video URL: ")
Download(url)