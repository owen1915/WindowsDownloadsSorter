#!/usr/bin/env python3

import os

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
os.chdir(downloads_path)

#make the directories to sort

sortedFoldersName = ["executables", "images", "videos", "misc", "pdfs", "zips", "audio", "txts", "dlls", "folders"]

for name in sortedFoldersName:
    try:
        os.mkdir(name)
    except FileExistsError:
        print("%s Folder already exits" % name)

# sort all the files based on there extension
for file in os.listdir(downloads_path):
    # get the extension
    filetype = file.split(".")
    if filetype[-1] == "exe" or filetype[-1] == "jar":
        os.rename(file, "executables/%s" % file)
    elif filetype[-1] == "jpg" or filetype[-1] == "png" or filetype[-1] == "gif" or filetype[-1] == "webp":
        os.rename(file, "images/%s" % file)
    elif filetype[-1] == "mp4":
        os.rename(file, "videos/%s" % file)
    elif filetype[-1] == "pdf" or filetype[-1] == "docx":
        os.rename(file, "pdfs/%s" % file)
    elif filetype[-1] == "zip" or filetype[-1] == "tar":
        os.rename(file, "zips/%s" % file)
    elif filetype[-1] == "mp3" or filetype[-1] == "wav":
        os.rename(file, "audio/%s" % file)
    elif filetype[-1] == "txt" or filetype[-1] == "csv":
        os.rename(file, "txts/%s" % file)
    elif filetype[-1] == "dll" or filetype[-1] == "config":
        os.rename(file, "dlls/%s" % file)
    elif not file.__contains__("."):
        if not sortedFoldersName.__contains__(file):
            os.rename(file, "folders/%s" % file)
    else:
        os.rename(file, "misc/%s" % file)