import os

print("1: yt-dlp")
print("2: ffmpeg convert")

menu = input("Select an option: ")

if menu == "1":
    URL = input("Paste your YT Link: ")
    output = input("Name the file: ")

    os.system(""" yt-dlp -f "bestaudio[ext=wav]/bestaudio" "{}" -o "output.%(ext)s" """.format(URL))
    os.system("ffmpeg -i output.webm output.wav")
    os.remove("output.webm")
    os.rename("output.wav", "{}.wav".format(output))
elif menu == "2":
    print ("Choose your input type:")
    print ("1. Image")
    print ("2. Video")
    print ("3. Audio")
    inptype = input ("...")

    if inptype == "1":
        print ("Choose your input format:")
        print ("1. png")
        print ("2. jpg")
        print ("3. webp")
        imagetype = input ("...")
        if imagetype == "1":
            option = "png"
        if imagetype == "2":
            option = "jpg"
        if imagetype == "3":
            option = "webp"

    if inptype == "2":
        print ("Choose your input format:")
        print ("1. mp4")
        print ("2. mkv")
        print ("3. mov")
        imagetype = input ("...")
        if imagetype == "1":
            option = "mp4"
        if imagetype == "2":
            option = "mkv"
        if imagetype == "3":
            option = "mov"
    
    if inptype == "3":
        print ("Choose your input format:")
        print ("1. wav")
        print ("2. mp3")
        print ("3. flac")
        imagetype = input ("...")
        if imagetype == "1":
            option = "wav"
        if imagetype == "2":
            option = "mp3"
        if imagetype == "3":
            option = "flac"

    print ("Choose your output type:")
    print ("1. Image")
    print ("2. Video")
    print ("3. Audio")
    inptype = input ("...")

    if inptype == "1":
        print ("Choose your output format:")
        print ("1. png")
        print ("2. jpg")
        print ("3. webp")
        imagetype = input ("...")
        if imagetype == "1":
            choice = "png"
        if imagetype == "2":
            choice = "jpg"
        if imagetype == "3":
            choice = "webp"

    if inptype == "2":
        print ("Choose your output format:")
        print ("1. mp4")
        print ("2. mkv")
        print ("3. mov")
        imagetype = input ("...")
        if imagetype == "1":
            choice = "mp4"
        if imagetype == "2":
            choice = "mkv"
        if imagetype == "3":
            choice = "mov"
    
    if inptype == "3":
        print ("Choose your output format:")
        print ("1. wav")
        print ("2. mp3")
        print ("3. flac")
        imagetype = input ("...")
        if imagetype == "1":
            choice = "wav"
        if imagetype == "2":
            choice = "mp3"
        if imagetype == "3":
            choice = "flac"

    file1 = "1." + option
    file2 = "2." + choice
    os.system("ffmpeg -i " + file1 + " " + file2)  