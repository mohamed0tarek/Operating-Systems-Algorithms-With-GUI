import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

class Task:
    def __init__(self, name, arrival_time, period_time, execution_time, deadline_time):
        self.name = name
        self.arrival_time = arrival_time
        self.period_time = period_time
        self.execution_time = execution_time
        self.deadline_time = deadline_time

    def __str__(self):
        return self.name


def add_task_entry():
    name = task_name_entry.get()
    arrival_time = int(arrival_time_entry.get())
    period_time = int(period_time_entry.get())
    execution_time = int(execution_time_entry.get())
    deadline_time = arrival_time + period_time

    task = Task(name, arrival_time, period_time, execution_time, deadline_time)
    tasks.append(task)
    task_listbox.insert(0, task.name)

    # Clear the task entry fields
    task_name_entry.delete(0, tk.END)
    arrival_time_entry.delete(0, tk.END)
    period_time_entry.delete(0, tk.END)
    execution_time_entry.delete(0, tk.END)


import matplotlib.pyplot as plt
import numpy as np
import random

def run_scheduler():
    current_time = 0
    task_queue = sorted(tasks, key=lambda x: (x.arrival_time, x.execution_time))
    timeline = []
    labels = []
    color_map = {}
    colors = ['yellow', 'lightblue', 'lightgreen', 'while', 'blue', 'orange', 'pink']
    counter = 0
    while current_time <= 30 and task_queue:
        task = task_queue.pop(0)
        if current_time < task.arrival_time:
            current_time = task.arrival_time
        start_time = current_time
        end_time = current_time + task.execution_time

        if end_time > task.deadline_time:
            color = 'red'
            timeline.append((start_time, end_time, color))
            labels.append(f"{task.name} (Deadline Broken)")
        else:
            if task.name not in color_map:
                # Generate a random color for the task
                color = colors[counter]
                color_map[task.name] = color
                counter += 1
            else:
                color = color_map[task.name]
            
            timeline.append((start_time, end_time, color))
            labels.append(task.name)

        current_time += task.execution_time
        task.arrival_time += task.period_time
        task.deadline_time = task.arrival_time + task.period_time
        task_queue.append(task)
        task_queue = sorted(tasks, key=lambda x: (x.arrival_time, x.execution_time))

        if current_time >= 30:
            break

    # Plotting the timeline
    fig, ax = plt.subplots()
    ax.set_ylim(0, 1)
    ax.set_xlim(0, 30)
    ax.set_xticks(range(0, 30, 2))  # Set x-ticks at 2, 4, 6, 8, ...
    for i, (start, end, color) in enumerate(timeline):
        ax.plot([start+1, end+1], [0, 0], color=color, lw=30)
        ax.text(start, 0.03, labels[i], ha='left', va='center')

    # ax.set_yticks([])
    ax.set_xlabel('Time')
    ax.set_title('Task Timeline')

    plt.show()



# Create the main window
window = tk.Tk()
window.title("FIFO Scheduler")
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

# FIFO Scheduler button
scheduler_button = ttk.Button(window, text="Run FIFO Scheduler", command=run_scheduler)
scheduler_button.pack(pady=10)

# Create an empty list to store tasks
tasks = []

# Start the main loop
window.mainloop()
