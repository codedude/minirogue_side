#!/usr/bin/env/ python3.5
#-*- coding: utf-8 -*-
#

try:
    import sys, os
    import tkinter as tk
    import tkinter.ttk as ttk
    import tkinter.filedialog as fd
    from shutil import copyfile
    from PIL import Image, ImageTk

except ImportError as e:
    print("Failed to load modules : {0}".format(e))
    sys.exit(2)


PATH_SAVE = os.getcwd() + "/Photos to print/"
HEIGHT, WIDTH = 0, 0
img_s = dict()
img_id = {"curr" : 0, "max" : 0, "dir" : "None"}

def changeImg(files, path, canvas, window):
    src_t = path+files[img_id["curr"]]
    dir_t = os.path.normpath(src_t).split(os.sep)[-2] + ' - '
    dest_t = PATH_SAVE+dir_t+files[img_id["curr"]]
    if not os.path.isfile(dest_t):
        window.title(src_t)
    else:
        window.title("Photo already SAVED")
    image = Image.open(path+files[img_id["curr"]])
    image.thumbnail((WIDTH, HEIGHT), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    img_s["s"] = image
    canvas.itemconfig(img_s["d"], image=image)


def saveImg(files, path, window):
    src_t = path+files[img_id["curr"]]
    dir_t = os.path.normpath(src_t).split(os.sep)[-2] + ' - '
    dest_t = PATH_SAVE+dir_t+files[img_id["curr"]]
    if not os.path.isfile(dest_t):
        copyfile(src_t, dest_t)
        window.title("Photo already SAVED")
        print("Save img : %s" % (dest_t))
    else:
        os.remove(dest_t)
        window.title(src_t)
        print("Delete img : %s" % (dest_t))



def popup(root, path):
    files = getFileList(path)
    if len(files) == 0:
        return
    img_id["max"] = len(files) - 1
    img_id["curr"] = 0

    window = tk.Toplevel(root)
    window.grid_rowconfigure(2, weight=1)
    window.grid_columnconfigure(2, weight=1)

    canvasImg = tk.Canvas(window, width=WIDTH, height=HEIGHT)
    window.title(path+files[img_id["curr"]])
    image = Image.open(path+files[img_id["curr"]])
    image.thumbnail((WIDTH, HEIGHT), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    img_s["s"] = image
    img_s["d"] = canvasImg.create_image(WIDTH/2, HEIGHT/2, anchor=tk.CENTER, image=image)

    def prevFile():
        if img_id["curr"] == 0:
            img_id["curr"] = img_id["max"]
        else:
            img_id["curr"] -= 1
        changeImg(files, path, canvasImg, window)
    def nextFile():
        if img_id["curr"] == img_id["max"]:
            img_id["curr"] = 0
        else:
            img_id["curr"] += 1
        changeImg(files, path, canvasImg, window)

    prevB = tk.Button(window, text="Previous", command=prevFile,
        padx=5, pady=5)
    nextB = tk.Button(window, text="Next", command=nextFile,
        padx=5, pady=5)

    prevB.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
    nextB.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
    canvasImg.grid(row=1, columnspan=2, padx=5, pady=5)

    def saveImgE(event):
        saveImg(files, path, window)
    window.bind('<space>', saveImgE)

def getFileList(path):
    print("-> Current dir : %s" % (path))
    fileList = list()
    dirs = os.scandir(path)
    for entry in dirs:
        if not entry.name.startswith('.'):
            if entry.is_file():
                fileList.append(entry.name)

    fileList = list(filter(lambda x :
        False if x.split('.')[-1] == '.JPG' else True, fileList))
    print("%d files found\n" % (len(fileList)))
    return fileList


def askFolder(root):
    filename = fd.askdirectory(title="Select A Folder", mustexist=1,
        initialdir="/home/valentin/Pictures/114_0111")
    if not filename == "":
        popup(root, filename+'/')


if __name__ == '__main__':
    print("App is launching...\n")

     #Init window
    app = tk.Tk()
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    app.title("AlbumPicker")

    WIDTH = app.winfo_screenwidth() - 200
    HEIGHT = app.winfo_screenheight() - 200

    #Closure
    def folderRoot():
        askFolder(app)
    b = tk.Button(app, text="Choisir un dossier", command=folderRoot,
        padx=50, pady=50)
    b.pack()

    app.mainloop()

    print("\nApp is now closing...")
    sys.exit(0)