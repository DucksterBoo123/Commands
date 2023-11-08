import os

print("1: yt-dlp")
print("2: ffmpeg convert")
print("3: macrecovery")
print("U: update executables")
menu = input("Select an option: ")
#UPDATER
if menu == "U":
    os.system("python3 updater.py")
    os.system("python3 commands.py")
#YTDOWNLOADER
elif menu == "1":
    URL = input("Paste your YT Link: ")
    output = input("Name the file: ")
    os.system(""" yt-dlp -f "bestaudio[ext=wav]/bestaudio" "{}" -o "output.%(ext)s" """.format(URL))
    os.system("ffmpeg -i output.webm output.wav")
    os.remove("output.webm")
    os.rename("output.wav", "{}.wav".format(output))
#FFMPEG
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
    os.system("/opt/homebrew/bin/ffmpeg -i " + file1 + " " + file2)
elif menu == "3":
    string1 = None
    string2 = None

    print("Pick a Version:")
    print("1. Lion")
    print("2. Mountain Lion")
    print("3. Mavericks")
    print("4. Yosemite")
    print("5. El Capitan")
    print("6. Sierra")
    print("7. High Sierra")
    print("8. Mojave")
    print("9. Catalina")
    print("10. Big Sur")
    print("11. Monterey")
    print("12. Ventura")
    ver = input("...")
    if ver == "1":
        string1 = "Mac-2E6FAB96566FE58C"
        string2 = "00000000000F25Y00"
    if ver == "2":
        string1 = "Mac-7DF2A3B5E5D671ED"
        string2 = "00000000000F65100"
    if ver == "3":
        string1 = "Mac-F60DEB81FF30ACF6"
        string2 = "00000000000FNN100"
    if ver == "4":
        string1 = "Mac-E43C1C25D4880AD6"
        string2 = "00000000000GDVW00"
    if ver == "5":
        string1 = "Mac-FFE5EF870D7BA81A"
        string2 = "00000000000GQRX00"
    if ver == "6":
        string1 = "Mac-77F17D7DA9285301"
        string2 = "00000000000J0DX00"
    if ver == "7":
        string1 = "Mac-7BA5B2D9E42DDD94"
        string2 = "00000000000J80300"
    if ver == "8":
        string1 = "Mac-7BA5B2DFE22DDD8C"
        string2 = "00000000000KXPG00"
    if ver == "9":
        string1 = "Mac-00BE6ED71E35EB86"
        string2 = "00000000000000000"
    if ver == "10":
        string1 = "Mac-42FD25EABCABB274"
        string2 = "00000000000000000"
    if ver == "11":
        string1 = "Mac-FFE5EF870D7BA81A"
        string2 = "00000000000000000"
    if ver == "12":
        string1 = "Mac-4B682C642B45593E"
        string2 = "00000000000000000"
    os.system("python3 macrecovery.py -b " + string1 + " -m " + string2 + " download")
#Throw and Callback
else:
    print("not an option")
    os.system("python3 commands.py")