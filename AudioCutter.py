from pydub import AudioSegment

AudioSegment.ffmpeg = "/absolute/path/to/ffmpeg"


def cutter(file_path, savefolder, cutsec = 10):
    # adding mp3 file into song object
    song = AudioSegment.from_file(file_path, format="mp3")

    i = 0
    j = 1
    # create starting and ending index
    startsec = i * 1000
    endsec = (i+int(cutsec)) * 1000
    
    while endsec<len(song):
        # cut song into cutsec time
        cutSong = song[startsec:endsec]
        cutSong.export(savefolder+"/"+str(j)+".mp3", format="mp3")
        # printing that jth file is saved
        print(str(j)+" Audio file is created and saved")

        # increement all veriable
        j+=1
        i+=int(cutsec)
        startsec = i * 1000
        endsec = (i+int(cutsec)) * 1000
    
    # last part which lenght is not equal cutset 
    cutSong = song[startsec:]
    cutSong.export(savefolder+"/"+str(j)+".mp3", format="mp3")

    # Program fully excute messaeg
    print("All file are save")

# example
cutter('funny123.mp3', 'data/5 sec/tried', 7)
