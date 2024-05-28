import tkinter as tk
import tkinter.filedialog

# main window screen
window = tk.Tk()
window.geometry("500x500")
file_name = ""
window.title("FTEdit - Text Editor: " + file_name)
window.resizable(True, True)

# window of window thingie
window2 = tk.Tk()
window2.title("FTEdit - Panel")

# about window screen
def about():
    aboutWindow = tk.Tk()
    aboutWindow.resizable(False, False)
    aboutWindow.title("FTEdit - About")
    labelthingie = tk.Label(master=aboutWindow, text="FTEdit is a simple, lightweight make text, edit file tool\nFTEdit Made by Huy1234TH\nVersion: 1.1.0")
    labelthingie.pack()    
    aboutWindow.mainloop()

aboutButton = tk.Button(
    text="About",master=window2
)
aboutButton.config(command=about)
aboutButton.place()
aboutButton.pack(fill=tk.BOTH)

# save button
def saveFile():
    file_path = tk.filedialog.asksaveasfilename(defaultextension='.txt')
    if file_path:
        content = entryTable.get("1.0", tk.END)
        with open(file_path, 'w') as file:
            file.write(content)
    
saveButton = tk.Button(
    text="Save",master=window2
)
saveButton.config(command=saveFile)
saveButton.place()
saveButton.pack(fill=tk.BOTH)

# load button
def loadFile():
    file_path = tk.filedialog.askopenfilename()
    if file_path:
        file_extension = file_path.split(".")[-1]
        if file_extension.lower() in ["exe", "msi"]:
            result = tk.messagebox.askyesno("FTEdit - Warning", "Are you sure you want to load the executable file?")
            if result:
                pass
            else:
                return
        with open(file_path, 'r') as file:
            content = file.read()
            entryTable.delete("1.0", tk.END)
            entryTable.insert("1.0", content)
    file_name = file_path


loadButton = tk.Button(
    master=window2,text="Load"
)
loadButton.config(command=loadFile)
loadButton.place()
loadButton.pack(fill=tk.BOTH)

# check if the window2 is exited, if not, then close the window
def on_closing():
    if window2.state() == "normal":
        window2.destroy()
    else:
        window2.destroy()
        window.destroy()

window2.protocol("WM_DELETE_WINDOW", on_closing)

# entry table
entryTable = tk.Text()
entryTable.master = window
entryTable.pack(fill=tk.BOTH, expand=True)

# main loop
window2.mainloop()
window.mainloop()