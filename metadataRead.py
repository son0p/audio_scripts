import eyed3
audiofile = eyed3.load("beat.mp3")
print audiofile.tag.artist
print audiofile.tag.bpm
