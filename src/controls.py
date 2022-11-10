import tkinter as tk

def delete(input: tk.Entry) -> None : # pragma: no cover
    if input["fg"] != "tomato": # delete text only if it's the message error
     return
    
    input.config(state="normal") # active the button
    input.delete(0, tk.END)
    input.config(fg="black", highlightbackground = "white", highlightcolor = "white") # return to the initial configuration
    return

def validate(input: tk.Entry) -> bool : # pragma: no cover
    if input.get() == "": 
        input.config(fg="tomato", highlightbackground = "red", highlightcolor = "red") # error configuration
        input.insert(0, "Required Field!") # error message
        input.config(state= "disabled", disabledforeground="red", disabledbackground="white") # disable the input
        return False
    
    if str(input) == ".input.gender":
        if(input.get() != "M" and input.get() != "F" and input.get() != "m" and input.get() != "f"):
            input.config(fg="tomato", highlightbackground = "red", highlightcolor = "red")
            input.delete(0, tk.END)
            input.insert(0, "Error, type M or F!")
            input.config(state="disabled", disabledforeground="red", disabledbackground="white")  
            return False
        
        return True
    
    if (input.winfo_parent() != ".start" and (input.get().isalpha() or not input.get().isnumeric() or input.get() == "0")):
        if str(input) == ".input.workout_time" and input.get() == "0": # workout time can be 0
            return True

        input.config(fg="tomato", highlightbackground = "red", highlightcolor = "red")
        input.delete(0, tk.END)
        input.insert(0, "Error, insert an integer > 0!")
        input.config(state= "disabled", disabledforeground="red", disabledbackground="white")  
        return False 
    
    if input["fg"] == "tomato": # if it's not valid
        return False
    
    return True

import input_page 
import result_page 

def go_back(root: tk.Tk, current_page: result_page.ResultPage, previous_page: input_page.InputPage) -> None: # pragma: no cover
    current_page.frame.destroy() 
    del current_page 
    previous_page.frame.grid(sticky="NSWE") # restore the previous page
    restore_event(root,previous_page) # restore the event of the previous page
    return

def restore_event(root: tk.Tk, page: input_page.InputPage) -> None: # pragma: no cover    
    root.unbind("<Return>")
    root.unbind("<BackSpace>")
    root.bind("<Return>", lambda f: page.send_input.invoke())
    page.age_input.focus_set()
    return