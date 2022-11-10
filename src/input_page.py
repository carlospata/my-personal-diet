import tkinter as tk
import start_page as previous
import controls as ctrl

class InputPage(): # pragma: no cover
    def __init__(self, parent: tk.Tk, previous_page: previous.StartGUI):       
        if not ctrl.validate(previous_page.name_input) : # verify the input from the previous page
            return
        
        previous_page.frame.grid_remove() # if, it's ok remove the previous page & create the new
        
        parent.unbind("<Return>") # unbind event about the previous page
        
        name = previous_page.name_input.get()

        # input page
        self.frame = tk.Frame(parent, bg="yellow", name="input")
        self.frame.grid(sticky="NSWE")

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(6, weight=1)

        # info 
        self.info_msg = tk.Label(self.frame, text="Hi " + name + ", now insert your data", 
                                 bg="yellow", font="Bazooka 18 bold")
        self.info_msg.grid(row=0, column=0, columnspan=2, sticky="WES", pady=(0,5))

        # age
        self.age = tk.Label(self.frame, text="Age: ", font="Arial 13",  bg="yellow")
        self.age.grid(row=1, column=0, sticky="E", pady=(0,5))
        
        self.age_input = tk.Entry(self.frame, font="Arial 13", width=23, highlightthickness=1)
        self.age_input.grid(row=1, column=1, sticky="W", pady=(0,5))
        self.age_input.bind("<Enter>", lambda f: ctrl.delete(self.age_input))
        self.age_input.bind("<Button-1>", lambda f: ctrl.delete(self.age_input))
        self.age_input.focus_set()

        # gender
        self.gender = tk.Label(self.frame, text="Gender (M or F): ", font="Arial 13", bg="yellow")
        self.gender.grid(row=2, column=0, sticky="E", pady=(0,5))
        
        self.gender_input = tk.Entry(self.frame, name="gender", font="Arial 13", width=23, highlightthickness=1)
        self.gender_input.grid(row=2, column=1, sticky="W", pady=(0,5))
        self.gender_input.bind("<Enter>", lambda f: ctrl.delete(self.gender_input))
        self.gender_input.bind("<Button-1>", lambda f: ctrl.delete(self.gender_input))
                
        # weight
        self.weight = tk.Label(self.frame, text="Weight (kg): ", font="Arial 13", bg="yellow")
        self.weight.grid(row=3, column=0, sticky="E", pady=(0,5))
        
        self.weight_input = tk.Entry(self.frame, font="Arial 13", width=23, highlightthickness=1)
        self.weight_input.grid(row=3, column=1, sticky="W", pady=(0,5))
        self.weight_input.bind("<Enter>", lambda f: ctrl.delete(self.weight_input))
        self.weight_input.bind("<Button-1>", lambda f: ctrl.delete(self.weight_input))
        
        # height
        self.height = tk.Label(self.frame, text="Height (cm): ", font="Arial 13", bg="yellow")
        self.height.grid(row=4, column=0, sticky="E", pady=(0,5))
        
        self.height_input = tk.Entry(self.frame, font="Arial 13", width=23, highlightthickness=1)
        self.height_input.grid(row=4, column=1, sticky="W", pady=(0,5))
        self.height_input.bind("<Enter>", lambda f: ctrl.delete(self.height_input))
        self.height_input.bind("<Button-1>", lambda f: ctrl.delete(self.height_input))
                
        # workout time
        self.workout_time = tk.Label(self.frame, text="Workout time (min/week): ", font="Arial 13", bg="yellow")
        self.workout_time.grid(row=5, column=0, sticky="E")
        
        self.workout_time_input = tk.Entry(self.frame, name="workout_time", font="Arial 13", width=23, highlightthickness=1)
        self.workout_time_input.grid(row=5, column=1, sticky="W")
        self.workout_time_input.bind("<Enter>", lambda f: ctrl.delete(self.workout_time_input))
        self.workout_time_input.bind("<Button-1>", lambda f: ctrl.delete(self.workout_time_input))

        import result_page as next
         
        # input button
        self.send_input = tk.Button(self.frame, name="send", text="Show your ideal diet!", font="Arial 15", borderwidth=1, 
                                    command=lambda: next.ResultPage(parent,self,name)) # pass to the next page
        self.send_input.grid(row=6, column=0, columnspan=2, sticky="N", pady=(10,0))
        
        parent.bind("<Return>", lambda f: self.send_input.invoke())
        
        # movement beetwen inputs with keyboard
        self.age_input.bind("<Down>", lambda f: self.gender_input.focus_set())
        self.gender_input.bind("<Up>", lambda f: self.age_input.focus_set())
        self.gender_input.bind("<Down>", lambda f: self.weight_input.focus_set())
        self.weight_input.bind("<Up>", lambda f: self.gender_input.focus_set())
        self.weight_input.bind("<Down>", lambda f: self.height_input.focus_set())
        self.height_input.bind("<Up>", lambda f: self.weight_input.focus_set())
        self.height_input.bind("<Down>", lambda f: self.workout_time_input.focus_set())
        self.workout_time_input.bind("<Up>", lambda f: self.height_input.focus_set())
