import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

class Task:
    def __init__(self, name, arrival_time, period_time, execution_time, deadline_time):
        self.name = name
        self.arrival_time = arrival_time
        self.period_time = period_time
        self.execution_time = execution_time
        self.stored_execution_time = execution_time
        self.deadline_time = deadline_time
        self.release_time = arrival_time

    def get_next_job(self):
        return Task(self.name, self.arrival_time + self.period_time, self.period_time, self.execution_time, self.deadline_time)


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


def sched_rr():
    programTime = 10
    quantumTime = 0.25
    system_log = []  # (task, startTime, endTime)
    current_time = 0
    queue = sorted(tasks, key=lambda x: x.arrival_time)
    timeline = []
    labels = []
    color_map = {}
    colors = ['blue', 'lightblue', 'yellow', 'while', 'red', 'orange', 'lightgreen']
    counter = 0
    
    while current_time <= programTime:
        if len(queue) == 0:
            current_time += quantumTime
            continue

        # Number of ready tasks
        task_counter = 0
        for tas in queue:
            if tas.release_time <= current_time:
                task_counter += 1
            if tas.release_time == current_time:
                queue.remove(tas)
                queue.insert(0, tas)
        task = queue[0]

        if current_time >= task.release_time:
            try:
                task.execution_time -= quantumTime  # Decrement the execution time by the quantum time
                if task.execution_time < 0:
                    task.execution_time = 0
                system_log.append((task, current_time, current_time + quantumTime, ''))
                #timeline
                if task.name not in color_map:
                    # Generate a random color for the task
                    color = colors[counter]
                    color_map[task.name] = color
                    counter += 1
                else:
                    color = color_map[task.name]
            
                timeline.append((current_time, current_time + quantumTime, color))
                labels.append(task.name)

                if task.execution_time == 0:
                    task.release_time += task.period_time
                    task.execution_time = task.stored_execution_time
                    one = queue.pop(0)
                    queue.append(one)
                else:
                    tas = queue.pop(0)
                    queue.insert(task_counter - 1, tas)

                current_time += quantumTime
                # for T in done_tasks:
                #     if T.release_time == current_time:
                #         queue.append(T)

            except:
                print("Task", task.name, f" Exceeded Deadline")
                system_log.append((task, current_time, current_time + quantumTime, "DEADLINE"))
                break

        else:
            current_time += quantumTime
            # for T in done_tasks:
            #         if T.release_time == current_time:
            #             queue.append(T)

    # Plotting the timeline   (draw using logs better)
    fig, ax = plt.subplots()
    ax.set_ylim(0, .5)
    ax.set_xlim(0, 10)
    # ax.set_xticks(range(0, 30, 2))  # Set x-ticks at 2, 4, 6, 8, ...
    for i, (start, end, color) in enumerate(timeline):
        ax.plot([start+.3, end+.3], [0, 0], color=color, lw=50)
        ax.text(start, 0.03, labels[i], ha='left', va='center')

    # ax.set_yticks([])
    ax.set_xlabel('Time')
    ax.set_title('Task Timeline')

    plt.show()


    return system_log



# Create the main window
window = tk.Tk()
window.title("Round Robin Scheduler")
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

# RR Scheduler button
scheduler_button = ttk.Button(window, text="Run RR Scheduler", command=sched_rr)
scheduler_button.pack(pady=10)

# Create an empty list to store tasks
tasks = []

# Start the main loop
window.mainloop()



# tasks.append(Task(1, 0, 6, 2, 6))
# tasks.append(Task(2, 1, 8, 2, 8))
# tasks.append(Task(3, 2, 15, 4, 15))

# logs = sched_rr(tasks, programTime, quantumTime)
# for log in logs:
#     task, start_time, end_time, status = log
#     print(f"Task: {task.name}")
#     print(f"Start Time: {start_time}")
#     print(f"End Time: {end_time}")
#     print(f"Status: {status}")
#     print("-----")

