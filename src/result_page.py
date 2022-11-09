import tkinter as tk 
import functions as func
import input_page as previous
import controls as ctrl
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ResultPage(): # pragma: no cover
    def __init__(self, parent: tk.Tk, previous_page: previous.InputPage, name: str):
        valid_input = True
        
        if not ctrl.validate(previous_page.age_input): 
            valid_input = False

        if not ctrl.validate(previous_page.gender_input): 
            valid_input = False
        
        if not ctrl.validate(previous_page.weight_input): 
            valid_input = False
        
        if not ctrl.validate(previous_page.height_input):
            valid_input = False
        
        if not ctrl.validate(previous_page.workout_time_input):
            valid_input = False
        
        if not valid_input:
            return
        else:
            previous_page.frame.grid_remove()

        parent.unbind("<Return>")
       
        self.frame = tk.Frame(parent, bg="yellow")
        self.frame.grid(sticky="NSWE")
        
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=0)
        self.frame.grid_rowconfigure(2, weight=0)
        self.frame.grid_rowconfigure(3, weight=1)

        if(previous_page.gender_input.get().islower()):
         tmp = previous_page.gender_input.get()
         previous_page.gender_input.delete(0, tk.END)
         previous_page.gender_input.insert(0, tmp.upper())

        # elaborate results according to the inputs
        basal_metabolism = func.basal_metabolism(previous_page.gender_input.get(), int(previous_page.age_input.get()), int(previous_page.weight_input.get()))
        laf = func.laf(int(previous_page.workout_time_input.get()), previous_page.gender_input.get())
        calorie_requirement = func.calorie_requirement(basal_metabolism, laf)
        carbohydrates, fats, proteins = func.calories_division(calorie_requirement)
        bmi = func.bmi(int(previous_page.weight_input.get()), int(previous_page.height_input.get()))
        workout_time = func.getWorkoutTime(bmi)

        self.result_msg = tk.Label(self.frame, text= name+", your ideal diet (kcal) is: ", 
                            bg="yellow", font="Bazooka 18 bold")
        self.result_msg.grid(row=0, column=0, columnspan=2, sticky="WES", pady=(0,5))
        
        # ********** creating graph to show the results ***********
        listLabels = ['carbohydrates','fats','proteins'] 
        listValues = [carbohydrates,fats,proteins]
        fig = Figure(figsize=(3,2), dpi=100, facecolor="white") # image container
        ax = fig.add_subplot(111)
        
        # formatting labels of each slice (it's a pie graph)
        def make_autopct(values):
            def my_autopct(pct):
                total = sum(values)
                val = int(round(pct*total/100.0))
                return " {v:d}    \n ({p:1.0f}%)  ".format(p=pct,v=val)
            return my_autopct
        
        # create pie graph
        patches, texts, autotexts = ax.pie(listValues, radius=1, labels=listLabels, autopct=make_autopct(listValues), pctdistance=0.5, startangle=180)
        autotexts[0].set_fontsize(10)
        autotexts[1].set_fontsize(8)
        autotexts[2].set_fontsize(8)
        
        # add graph to the page
        self.chart1 = FigureCanvasTkAgg(fig,self.frame)
        self.chart1.get_tk_widget().grid(row=1, column=0, columnspan=2, sticky="S", pady=(0,5))
        
        # *************************************************************
        
        self.result_msg2 = tk.Label(self.frame, text="and, you should workout < " + str(workout_time) + " minutes > weekly", 
                                    bg="yellow", font="Bazooka 16 bold")
        self.result_msg2.grid(row=2, column=0, columnspan=2, sticky="WEN", pady=(10,20))
        
        self.back_btn = tk.Button(self.frame, text="Back", font="Arial 15", borderwidth=1,
                                  command=lambda: ctrl.go_back(parent,self,previous_page)) # go the the previous page
        self.back_btn.grid(row=3, column=0, sticky="NE", padx=(0,20))
        
        parent.bind("<BackSpace>", lambda f: self.back_btn.invoke())

        self.bye_btn = tk.Button(self.frame, text="Quit", font="Arial 15", borderwidth=1, 
                                 command=lambda: parent.destroy()) # quit the application & destroy all widgets
        self.bye_btn.grid(row=3, column=1, sticky="NW")
        
        parent.bind("<Return>", lambda f: self.bye_btn.invoke())