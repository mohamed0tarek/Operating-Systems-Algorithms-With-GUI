import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from queue import PriorityQueue

class Task:
    def __init__(self, name, arrival_time, period, execution_time, deadline):
        self.name = name
        self.arrival_time = arrival_time
        self.period = period
        self.execution_time = execution_time
        self.deadline = deadline
        self.stored_execution_time = execution_time
    
    def __lt__(self, other):
        return self.deadline < other.deadline
    
    def __repr__(self):
        return f"{self.name} {self.arrival_time} {self.execution_time}"


def add_task_entry():
    name = task_name_entry.get()
    arrival_time = int(arrival_time_entry.get())
    period_time = int(period_time_entry.get())
    execution_time = int(execution_time_entry.get())  
    deadline_time = int(deadline_time_entry.get())

    task = Task(name, arrival_time, period_time, execution_time, deadline_time)
    tasks.append(task)
    task_listbox.insert(0, task.name)

    # Clear the task entry fields
    task_name_entry.delete(0, tk.END)
    arrival_time_entry.delete(0, tk.END)
    period_time_entry.delete(0, tk.END)
    execution_time_entry.delete(0, tk.END)
    deadline_time_entry.delete(0, tk.END)



def run_scheduler():
    task_queue = sorted(tasks, key=lambda x: x.arrival_time)
    new_period = []
    timeline = []
    labels = []
    counter = 0
    color_map = {}
    colors = ['yellow', 'lightblue', 'lightgreen', 'while', 'blue', 'orange', 'pink']
    current_time = task_queue[0].arrival_time
    while current_time <= 70 and task_queue:
        flage = False
        for T in new_period:
            if current_time == T.arrival_time:
                new_period.remove(T)
                task_queue.append(T)
                task_queue = sorted(task_queue, key=lambda x: x.deadline)
        current_task = task_queue.pop(0)
        # if current_task.arrival_time > current_time:
        #     current_time = current_task.arrival_time
        while current_task.execution_time > 0:
            print(f"{current_task.name} executed from time  {current_time}  to  {current_time+1}")
            current_time += 1
            current_task.execution_time -= 1
            if current_task.name not in color_map:
                # Generate a random color for the task
                color = colors[counter]
                color_map[current_task.name] = color
                counter += 1
            else:
                color = color_map[current_task.name]
            
            timeline.append((current_time, current_time+1, color))
            labels.append(current_task.name)
            if current_time > current_task.deadline:
                print("Deadline missed!")
                return
            for T in task_queue:
                if current_time == T.arrival_time and current_task.deadline > T.deadline and current_task.execution_time > 0:
                    flage = True
                    task_queue.remove(T)
                    task_queue.insert(0, T)
                    task_queue.insert(1, current_task)
                    break
            if flage == True:
                break
        if current_task.execution_time <= 0:
            current_task.arrival_time +=current_task.period
            current_task.deadline += current_task.period
            current_task.execution_time = current_task.stored_execution_time
            new_period.append(current_task)

    # Plotting the timeline
    fig, ax = plt.subplots()
    ax.set_ylim(0, 1)
    ax.set_xlim(0, 70)
    ax.set_xticks(range(0, 70, 2))  # Set x-ticks at 2, 4, 6, 8, ...
    for i, (start, end, color) in enumerate(timeline):
        ax.plot([start+.1, end+.1], [0, 0], color=color, lw=30)
        ax.text(start-1, 0.03, labels[i], ha='left', va='center')

    # ax.set_yticks([])
    ax.set_xlabel('Time')
    ax.set_title('Task Timeline')

    plt.show()



# Create the main window
window = tk.Tk()
window.title("DMA Scheduler")
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

# deadline Time entry
deadline_time_label = ttk.Label(task_frame, text="deadline Time:")
deadline_time_label.grid(row=4, column=0, sticky=tk.W)
deadline_time_entry = ttk.Entry(task_frame)
deadline_time_entry.grid(row=4, column=1, sticky=tk.W)

# Add Task button
add_task_button = ttk.Button(task_frame, text="Add Task", command=add_task_entry)
add_task_button.grid(row=5, columnspan=2, pady=10)

# Task Listbox
task_listbox = tk.Listbox(window)
task_listbox.pack(padx=10, pady=10)

# Output Text
# output_text = tk.Text(window, height=10, width=40)
# output_text.pack(padx=10, pady=10)

# FCFS Scheduler button
scheduler_button = ttk.Button(window, text="Run DMA Scheduler", command=run_scheduler)
scheduler_button.pack(pady=10)

# Create an empty list to store tasks
tasks = []

taskss = [
    Task(1, 0, 60, 25, 50),
    Task(2, 15, 60, 10, 40),
    Task(3, 20, 60, 15, 60),
]

# Start the main loop
window.mainloop()

