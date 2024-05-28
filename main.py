import tkinter as tk
import tkinter.filedialog

# main window screen
window = tk.Tk()
window.geometry("500x500")
window.title("FTEdit")
window.resizable(False, False)


# frame window screen
frame = tk.Frame(master=window)
frame.pack(fill=tk.BOTH, expand=True)

# save button
def saveFile():
    file_path = tk.filedialog.asksaveasfilename(defaultextension='.txt')
    if file_path:
        content = entryTable.get("1.0", tk.END)
        with open(file_path, 'w') as file:
            file.write(content)
    
saveButton = tk.Button(
    text="Save",borderwidth=5,master=frame
)
saveButton.config(command=saveFile)
saveButton.place(relx=0.15, rely=0.3, anchor=tk.CENTER)

# load button
def loadFile():
    file_path = tk.filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            entryTable.delete("1.0", tk.END)
            entryTable.insert("1.0", content)

loadButton = tk.Button(
    master=frame,text="Load",borderwidth=5
)
loadButton.config(command=loadFile)
loadButton.place(relx=0.05, rely=0.3, anchor=tk.CENTER)

# entry table
entryTable = tk.Text()
entryTable.master = window
entryTable.pack(fill=tk.BOTH, expand=True)

# main loop
window.mainloop()