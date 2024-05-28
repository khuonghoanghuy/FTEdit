import tkinter as tk
import tkinter.filedialog

# main window screen
window = tk.Tk()
window.geometry("500x500")
window.title("FTEdit")

# save button
def saveFile():
    file_path = tk.filedialog.asksaveasfilename(defaultextension='.txt')
    if file_path:
        content = entryTable.get("1.0", tk.END)
        with open(file_path, 'w') as file:
            file.write(content)
    
saveButton = tk.Button(master=window, text="Save")
saveButton.config(command=saveFile)
saveButton.pack()

# load button
def loadFile():
    file_path = tk.filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            entryTable.delete("1.0", tk.END)
            entryTable.insert("1.0", content)

loadButton = tk.Button(master=window, text="Load")
loadButton.config(command=loadFile)
loadButton.pack()

# entry table
entryTable = tk.Text()
entryTable.master = window
entryTable.pack(fill="both", expand=True)

# main loop
window.mainloop()