import os
import eyed3

mp3_dir = '/path/to/mp3/dir'
mp3_list = os.listdir(mp3_dir)

track_num = 0
for line in mp3_list:
    mp3_path = os.path.join(mp3_dir, line)
    print(mp3_path)

    track_num += 1
    audiofile = eyed3.load(mp3_path)
    audiofile.tag.artist = u"Artist"
    audiofile.tag.album = u"Album Name"
    audiofile.tag.album_artist = u"Various Artists"
    audiofile.tag.title = u"Title Name"
    audiofile.tag.track_num = track_num

    audiofile.tag.save()
