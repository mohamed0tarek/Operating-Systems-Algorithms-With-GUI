import tkinter as tk

def rma_bound_test(tasks):
    """Performs a bound test to check if the tasks are schedulable using the RMA algorithm.
    Returns True if schedulable, False otherwise."""
    
    n = len(tasks)
    utilization = sum(task['execution'] / task['period'] for task in tasks)
    bound = n * ((2 ** (1/n)) - 1)
    
    if utilization <= bound:
        return True
    else:
        return False

def add_task():
    """Adds a new task to the task list."""
    
    task = {'arrived': int(arrived_entry.get()),
            'period': int(period_entry.get()),
            'execution': int(execution_entry.get()),
            'deadline': int(deadline_entry.get()),
            'Name': int(constrictor_entry.get())}
    tasks.append(task)
    task_listbox.insert(tk.END, task)
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

def run_rma():
    """Runs the RMA bound test and displays the result."""
    
    if rma_bound_test(tasks):
        result_label.config(text="Schedulable using RMA!", font=('', 11))
    else:
        result_label.config(text="Not schedulable using RMA.", font=('', 11))

# Create the main window
root = tk.Tk()
root.title("RMA Bound Test")
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
run_button = tk.Button(root, text="Run RMA_bound_test", command=run_rma)
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