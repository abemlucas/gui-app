import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

# Reads the txt file and saves each app on a different line.

if os.path.isfile('opened_apps.txt'):
    with open('opened_apps.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')

        apps = [x for x in tempApps if x.strip()]


# Function for adding the apps on the frame connects to the openFile button.


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

# Function for running the apps related to the runApps button.


def runApps():
    for app in apps:
        os.startfile(app)


# set up the Canvas of the display screen.
canvas = tk.Canvas(root, height=450, width=450, bg="black")
canvas.pack()

# set up Frame of the display screen.
frame = tk.Frame(root, bg="black")
frame.place(relwidth=1.0, relheight=1.0, relx=0.0, rely=0.0)

# Initialize the variable for the button openFile.
openFile = tk.Button(root, text="Open Files", padx=10,
                     pady=5, fg="white", bg="red", command=addApp)
openFile.pack()

# Initialize the variable for the button runApps.
runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="red", command=runApps)
runApps.pack()


# Saves the selected apps for the next-time execution.
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# Stores the opened apps in the txt file.
with open('opened_apps.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
