import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import random

class Task:
    def __init__(self, name, execution_time, deadline, period, arrival_time):
        self.name = name
        self.execution_time = execution_time
        self.deadline = deadline
        self.period = period
        self.arrival_time = arrival_time

def run_scheduler():
    def schedule(tasks):
        tasks = pd.DataFrame.from_dict(tasks, orient='index')
        tasks['current_execution_time'] = tasks['execution_time']
        tasks['current_deadline'] = tasks['deadline']
        timeline = []

        for i in range(np.lcm.reduce(tasks['period'])):
            arrived_tasks = tasks[(tasks['arrival_time'] <= i) & (tasks['current_execution_time'] > 0)]

            if not arrived_tasks.empty:
                top_task = arrived_tasks.sort_values('current_deadline').index[0]
                tasks.loc[top_task, 'current_execution_time'] -= 1

                if timeline and timeline[-1]['task'] == top_task and timeline[-1]['end'] == i:
                    timeline[-1]['end'] = i + 1
                    timeline[-1]['length'] += 1
                else:
                    timeline.append({'task': top_task, 'start': i, 'end': i + 1, 'length': 1})

            arrived = tasks[(i + 1) % tasks['period'] == 0].index
            tasks.loc[arrived, 'current_execution_time'] = tasks.loc[arrived, 'execution_time']
            tasks.loc[arrived, 'current_deadline'] = tasks.loc[arrived, 'deadline'] + i + 2

        return pd.DataFrame(timeline)

    task_data = {}
    for task in tasks:
        task_data[task.name] = {
            'execution_time': task.execution_time,
            'deadline': task.deadline,
            'period': task.period,
            'arrival_time': task.arrival_time
        }

    timeline = schedule(task_data)

    canvas.delete("all")

    canvas_width = 1000
    canvas_height = 200
    setup_line_height = 20

    time_unit_width = canvas_width / timeline['end'].max()
    time_unit_height = (canvas_height - setup_line_height) / 2

    # Assign different colors to each task
    task_colors = {}
    for task_name in timeline['task'].unique():
        task_colors[task_name] = "#" + ("%06x" % random.randint(0, 0xFFFFFF))

    # Draw the timeline bars
    for i, row in timeline.iterrows():
        start = row['start']
        end = row['end']
        length = row['length']
        x = start * time_unit_width
        bar_width = length * time_unit_width
        bar_height = time_unit_height * 0.8
        task_name = row['task']
        task_color = task_colors[task_name]
        task_label = f"Task: {task_name}"
        task_label_width = len(task_label) * 7  # Adjust label width based on text length
        label_x = x + bar_width / 2 - task_label_width / 2
        label_y = canvas_height - setup_line_height + bar_height / 2

        canvas.create_rectangle(x, label_y - bar_height, x + bar_width, label_y, fill=task_color)
        canvas.create_text(label_x, label_y - bar_height / 2, text=task_label)

    # Draw setup line
    canvas.create_line(0, canvas_height - setup_line_height, canvas_width, canvas_height - setup_line_height)

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, timeline.to_string(index=False))


window = tk.Tk()
window.title("Scheduler GUI")

task_frame = ttk.LabelFrame(window, text="Add Task")
task_frame.pack(padx=10, pady=10)

task_name_label = ttk.Label(task_frame, text="Task Name:")
task_name_label.grid(row=0, column=0, sticky=tk.W)
task_name_entry = ttk.Entry(task_frame)
task_name_entry.grid(row=0, column=1, sticky=tk.W)

execution_time_label = ttk.Label(task_frame, text="Execution Time:")
execution_time_label.grid(row=1, column=0, sticky=tk.W)
execution_time_entry = ttk.Entry(task_frame)
execution_time_entry.grid(row=1, column=1, sticky=tk.W)

deadline_label = ttk.Label(task_frame, text="Deadline:")
deadline_label.grid(row=2, column=0, sticky=tk.W)
deadline_entry = ttk.Entry(task_frame)
deadline_entry.grid(row=2, column=1, sticky=tk.W)

period_label = ttk.Label(task_frame, text="Period:")
period_label.grid(row=3, column=0, sticky=tk.W)
period_entry = ttk.Entry(task_frame)
period_entry.grid(row=3, column=1, sticky=tk.W)

arrival_time_label = ttk.Label(task_frame, text="Arrival Time:")
arrival_time_label.grid(row=4, column=0, sticky=tk.W)
arrival_time_entry = ttk.Entry(task_frame)
arrival_time_entry.grid(row=4, column=1, sticky=tk.W)

def add_task():
    name = task_name_entry.get()
    execution_time = int(execution_time_entry.get())
    deadline = int(deadline_entry.get())
    period = int(period_entry.get())
    arrival_time = int(arrival_time_entry.get())
    task = Task(name, execution_time, deadline, period, arrival_time)
    tasks.append(task)
    task_listbox.insert(tk.END, name)
    clear_task_entry()

add_task_button = ttk.Button(task_frame, text="Add Task", command=add_task)
add_task_button.grid(row=5, column=0, columnspan=2, pady=10)

tasks = []
task_listbox = tk.Listbox(window, height=5)
task_listbox.pack(padx=10)

def clear_task_entry():
    task_name_entry.delete(0, tk.END)
    execution_time_entry.delete(0, tk.END)
    deadline_entry.delete(0, tk.END)
    period_entry.delete(0, tk.END)
    arrival_time_entry.delete(0, tk.END)

def remove_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        tasks.pop(selected_index[0])
        task_listbox.delete(selected_index[0])
        clear_task_entry()

remove_task_button = ttk.Button(window, text="Remove Task", command=remove_task)
remove_task_button.pack(pady=10)

canvas_frame = ttk.Frame(window)
canvas_frame.pack(padx=10, pady=10)

canvas_width = 1000
canvas_height = 200

canvas = tk.Canvas(canvas_frame, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

output_text = tk.Text(window, height=10)
output_text.pack(padx=10, pady=10)

run_scheduler_button = ttk.Button(window, text="Run Scheduler", command=run_scheduler)
run_scheduler_button.pack(pady=10)

window.mainloop()