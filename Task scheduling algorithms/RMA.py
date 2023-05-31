import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

def add_task_entry():
    name = str(task_name_entry.get())
    arrival_time = int(arrival_time_entry.get())
    period_time = int(period_time_entry.get())
    execution_time = int(execution_time_entry.get())
    deadline_time = arrival_time + period_time

    task = (arrival_time, period_time, execution_time, deadline_time, name)
    tasks.append(task)
    task_listbox.insert(0, task[4])

    # Clear the task entry fields
    task_name_entry.delete(0, tk.END)
    arrival_time_entry.delete(0, tk.END)
    period_time_entry.delete(0, tk.END)
    execution_time_entry.delete(0, tk.END)

def rma():
    # Sort tasks based on their period times
    queue = sorted(tasks, key=lambda x: x[1])
    schedule = []
    time = 0
    current_time=0
    while current_time <= 3 :
        for task in queue:
            # Calculate the number of instances of the task that should have occurred until this point in time
            n = int((time - task[0]) / task[1]) + 1
            # Calculate the deadline of the next instance of the task
            deadline = task[0] + n * task[1] + task[3]
            # If the deadline of the next instance of the task has not passed yet, schedule it
            if deadline > time:
                start_time = max(time, task[0] + (n - 1) * task[1])
                end_time = start_time + task[2]
                schedule.append((task[4], start_time, end_time))
                time = end_time
        current_time +=1       

    colors = {"1": "blue", "2": "green", "3": "red","4":"brown","5":"orange"}
    for task in schedule:
        plt.barh(y=task[0], left=task[1], width=task[2]-task[1], color=colors[task[0]], alpha=0.7)
    plt.yticks(list(colors.keys()))
    plt.xlabel("Time")
    plt.ylabel("Task")
    plt.title("RMA Schedule")
    plt.grid(axis='x')
    # Setting x-axis limits
    plt.xlim(0, 42)
    

    plt.show()
    
    # Example usage
# tasks = [(0, 24, 7, 24, 'A'), (0, 36, 12, 36, 'B'), (0, 48, 4, 48, 'C')]
# schedule = rma(tasks)

# Create the main window
window = tk.Tk()
window.title("RMA Scheduler")
window.geometry("400x500")

# Create task entry frame
task_frame = ttk.Frame(window)
task_frame.pack(padx=10, pady=10)

# Task Name entry
task_name_label = ttk.Label(task_frame, text="Task Name:")
task_name_label.grid(row=0, column=0, sticky=tk.W)
task_name_entry = ttk.Entry(task_frame)
task_name_entry.grid(row=0, column=1, sticky=tk.W)

# Arrival Time entry
arrival_time_label = ttk.Label(task_frame, text="Arrival Time:")
arrival_time_label.grid(row=1, column=0, sticky=tk.W)
arrival_time_entry = ttk.Entry(task_frame)
arrival_time_entry.grid(row=1, column=1, sticky=tk.W)

# Period Time entry
period_time_label = ttk.Label(task_frame, text="Period Time:")
period_time_label.grid(row=2, column=0, sticky=tk.W)
period_time_entry = ttk.Entry(task_frame)
period_time_entry.grid(row=2, column=1, sticky=tk.W)

# Execution Time entry
execution_time_label = ttk.Label(task_frame, text="Execution Time:")
execution_time_label.grid(row=3, column=0, sticky=tk.W)
execution_time_entry = ttk.Entry(task_frame)
execution_time_entry.grid(row=3, column=1, sticky=tk.W)

# Add Task button
add_task_button = ttk.Button(task_frame, text="Add Task", command=add_task_entry)
add_task_button.grid(row=4, columnspan=2, pady=10)

# Task Listbox
task_listbox = tk.Listbox(window)
task_listbox.pack(padx=10, pady=10)

# Output Text
# output_text = tk.Text(window, height=10, width=40)
# output_text.pack(padx=10, pady=10)

# RMA Scheduler button
scheduler_button = ttk.Button(window, text="Run RMA Scheduler", command=rma)
scheduler_button.pack(pady=10)

# Create an empty list to store tasks
tasks = []

# Start the main loop
window.mainloop()
        