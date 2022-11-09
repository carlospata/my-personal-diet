import tkinter as tk
import start_page as first

if __name__ == "__main__": # pragma: no cover
    root = tk.Tk() # root window
    root.title("My Personal Diet")
    root.geometry("550x400")
    root.resizable(True, True)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    first.StartGUI(root) # create the first page
    
    root.mainloop()
