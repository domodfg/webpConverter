#!/usr/bin/env python3

import os, sys
import tkinter as tk
from tkinter import filedialog
from PIL import Image


def import_file():
    infile = filedialog.askopenfilename(title="Select an image", filetypes=[("Webp image", "*.webp")])
    if infile:
        # Process the selected file (you can replace this with your own logic)
        f, e = os.path.splitext(infile)
        outfile = f + ".jpg"
        print(infile, outfile, f, e)
        if infile != outfile:
            try:
                with Image.open(infile) as im:
                    im.save(outfile)
                tk.messagebox.showinfo(title="Success", message="File saved to {outfile}".format(outfile=outfile))
            except OSError:
                tk.messagebox.showerror(title="Error", message="cannot convert {infile}".format(infile=infile))

            

def main():
    root = tk.Tk()  # create a root widget
    root.title("Webp to jpg converter")
    root.minsize(200, 200)  # width, height
    root.maxsize(500, 500)
    root.geometry("300x300+50+50")  # width x height + x + y

    round = tk.PhotoImage(file="button.png")
    import_button = tk.Button(root, image=round, command=import_file, border=0)
    import_button.pack(pady=50)

    root.mainloop()

if __name__ == "__main__":
    main()