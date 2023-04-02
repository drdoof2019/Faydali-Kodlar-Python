from moviepy.editor import *
import os
dir = '.'
allfiles = os.listdir(dir)
for fname in allfiles:
    if fname.endswith('.mp4'):
        print(fname)
        FILETOCONVERT = AudioFileClip(fname)
        FILETOCONVERT.write_audiofile(f"{fname}.mp3")
        FILETOCONVERT.close()