import tkinter as tk
import tkinter.filedialog

# main thing
versionApplication = "1.1.0"

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
    labelthingie = tk.Label(master=aboutWindow, text="FTEdit is a simple, lightweight make text, edit file tool\nFTEdit Made by Huy1234TH\nVersion: " + versionApplication)
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
    
    if not file_path:
        return
    
    file_extension = file_path.split(".")[-1].lower()
    if file_extension in ["exe", "msi"]:
        if not tk.messagebox.askyesno("FTEdit - Warning", "Are you sure you want to load the executable file?"):
            return
    
    with open(file_path, 'r') as file:
        content = file.read()
        entryTable.delete("1.0", tk.END)
        entryTable.insert("1.0", content)
    
    global file_name
    file_name = file_path


loadButton = tk.Button(
    master=window2,text="Load"
)
loadButton.config(command=loadFile)
loadButton.place()
loadButton.pack(fill=tk.BOTH)

def on_closing2():
    window2.destroy()
    window.destroy()
def on_closeing():
    window.destroy()
    window2.destroy()
window.protocol("WM_DELETE_WINDOW", on_closeing)
window2.protocol("WM_DELETE_WINDOW", on_closing2)

# entry table
entryTable = tk.Text()
entryTable.master = window
entryTable.pack(fill=tk.BOTH, expand=True)
entryTable.tag_configure("brackets", foreground="red")

def tag_brackets(event: tk.Event) -> None:
    try:
        text = entryTable.get("1.0", tk.END)
        if text is None:
            return
        text_list = list(text)
        if text_list is None:
            return
        count = 0
        for i in text_list:
            if i in ["{", "}", "(", ")", "[", "]", "'", '"']:
                entryTable.tag_add(
                    "brackets", "1.0+{0}c".format(count), "1.0+{0}c".format(count + 1)
                )
            count += 1
    except Exception as e:
        print(f"An error occurred: {e}")

entryTable.bind("<KeyRelease>", tag_brackets)

# main loop
window2.mainloop()
window.mainloop()