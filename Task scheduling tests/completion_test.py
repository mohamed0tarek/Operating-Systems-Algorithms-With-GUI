import tkinter as tk
from math import *

class Task:
    def __init__(self, name, arrival_time, period_time, execution_time, deadline_time):
        self.name = name
        self.arrival_time = arrival_time
        self.period_time = period_time
        self.execution_time = execution_time
        self.deadline_time = deadline_time


output = ""

def rma_completion_time_test(tasks):

    #Completion-Time test
    results = []
    global output
    count = 1
    for task in tasks:
        if(tasks.index(task)==0):
            #first task always schedulable
            results.append(True)
            continue
        else:
            taskIndex = tasks.index(task)

            t=task.execution_time
            for i in range(taskIndex):
                t += ceil(task.deadline_time/tasks[i].deadline_time) * tasks[i].execution_time
            
            if( t <= task.deadline_time ):
                #result_label.config(text=f"Tasks can not be scheduled without missing a deadline.")
                results.append(True)
            else:
                results.append(False)
                break
    for b in results:
        if b == True:
            output += f"T{count} is scheduable \n"
        else:
            output += f"T{count} can't be scheduable \n"
            
        count +=1
        
    result_label.config(text=output, font=('', 11))
    return results
        
    

def add_task():
    """Adds a new task to the task list."""
    
    arrived = float(arrived_entry.get())
    period = float(period_entry.get())
    execution = float(execution_entry.get())
    deadline = float(deadline_entry.get())
    Name =  int(constrictor_entry.get())

    task = Task(Name, arrived, period, execution, deadline)
    tasks.append(task)
    T = f"name: {Name}, arrive_time: {arrived}, period:{period}, deadline: {deadline}"
    task_listbox.insert(tk.END, T)
    clear_entries()

def remove_task():
    """Removes the selected task from the task list."""
    
    selection = task_listbox.curselection()
    if selection:
        index = selection[0]
        tasks.pop(index)
        task_listbox.delete(index)

def clear_entries():
    """Clears the task parameter entries."""
    
    arrived_entry.delete(0,tk.END)
    period_entry.delete(0, tk.END)
    execution_entry.delete(0, tk.END)
    deadline_entry.delete(0, tk.END)
    constrictor_entry.delete(0, tk.END)
    


# Create the main window
root = tk.Tk()
root.title("RMA ( Completion-Time Test )")
root.geometry("400x500")

# Create the task parameter input labels and entries
arrived_label = tk.Label(root, text="Arrived time:")
arrived_entry = tk.Entry(root)
period_label = tk.Label(root, text="Period:")
period_entry = tk.Entry(root)
execution_label = tk.Label(root, text="Execution time:")
execution_entry = tk.Entry(root)
deadline_label = tk.Label(root, text="Deadline:")
deadline_entry = tk.Entry(root)
constrictor_label = tk.Label(root, text="Name:")
constrictor_entry = tk.Entry(root)

# Create the task listbox and scrollbar
task_listbox = tk.Listbox(root, width=50)
task_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=task_listbox.yview)
task_listbox.config(yscrollcommand=task_scrollbar.set)

# Create the add and remove task buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)

# Create the run RMA button and result label
run_button = tk.Button(root, text="Run RMA_Completion_test", command= lambda : rma_completion_time_test(tasks))
result_label = tk.Label(root, text="")

# Add the widgets to the window using grid layout
arrived_label.grid(row=0, column=0, sticky=tk.E, padx=25)
arrived_entry.grid(row=0, column=1, pady=7)
period_label.grid(row=1, column=0, sticky=tk.E, padx=25)
period_entry.grid(row=1, column=1, pady=7)
execution_label.grid(row=2, column=0, sticky=tk.E, padx=25)
execution_entry.grid(row=2, column=1, pady=7)
deadline_label.grid(row=3, column=0, sticky=tk.E, padx=25)
deadline_entry.grid(row=3, column=1, pady=7)
constrictor_label.grid(row=4, column=0, sticky=tk.E, padx=25)
constrictor_entry.grid(row=4, column=1, pady=7)
add_button.grid(row=5, column=0, padx=25)
remove_button.grid(row=5, column=1, padx=25)
task_listbox.grid(row=6, column=0, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W, pady=7, padx=25)
task_scrollbar.grid(row=6, column=2, sticky=tk.N+tk.S)
run_button.grid(row=7, column=0, columnspan=2, pady=7, padx=25)
result_label.grid(row=8, column=0, columnspan=2, pady=7, padx=25)

# Create a list to store the tasks
tasks = []

# Start the main event loop
root.mainloop()