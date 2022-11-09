import tkinter as tk

class StartGUI(): # pragma: no cover
    def __init__(self, parent: tk.Tk):
        # start page
        self.frame = tk.Frame(parent, bg="yellow", name="start")
        self.frame.grid(sticky="NSWE")
        
        # distribute a specific weight to rows & columns
        self.frame.grid_columnconfigure(0, weight=1)  
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=0)
        self.frame.grid_rowconfigure(2, weight=1)
        
        # welcome message
        self.welcome_msg = tk.Label(self.frame, text="Hello!", font="Bazooka 25 bold", bg="yellow")
        self.welcome_msg.grid(row=0, column=0, columnspan=2, sticky="S", pady=(0,5))

        # name
        self.name = tk.Label(self.frame, text="Insert your name: ", font="Arial 13", bg="yellow")
        self.name.grid(row=1, column=0, sticky="NE", padx=(25,5))
        
        import controls as ctrl # [ import inside class to avoid CircularImport ]

        self.name_input = tk.Entry(self.frame, font="Arial 13", width=23, highlightthickness=1)
        self.name_input.grid(row=1, column=1, sticky="NW")
        self.name_input.focus_set() # direct the focus of the application to the widget
        self.name_input.bind("<Enter>", lambda f: ctrl.delete(self.name_input)) # bind an event to the widget
        self.name_input.bind("<Button-1>", lambda f: ctrl.delete(self.name_input))
        
        import input_page as next

        # enter
        self.enter = tk.Button(self.frame, text="Send", font="Arial 15", borderwidth=1, command=lambda: next.InputPage(parent,self)) # pass to the next page
        self.enter.grid(row=2, column=0, columnspan=2, sticky="N", pady=(10,0))
        
        parent.bind("<Return>", lambda f: self.enter.invoke()) # bind an event to the parent window