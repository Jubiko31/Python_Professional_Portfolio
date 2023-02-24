from moviepy.editor import *

videofile = VideoFileClip("<name>.mp4")
audiofile = videofile.audio
audiofile.write_audiofile("<name>.mp3")

videofile.close()
audiofile.close()