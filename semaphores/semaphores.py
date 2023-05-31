import threading
import tkinter as tk
import queue


class Semaphore:
    def __init__(self, initial_value):
        self.count = initial_value
        self.lock = threading.Condition()
    #The P method represents the "P" operation of the semaphore,
    #. It decreases the count by 1.
    #If the count becomes negative, it means that there are no available resources,
    #so the current thread waits by calling self.lock.wait().
    #The thread will be blocked until another thread calls the V method and releases a resource.
    def P(self):
        with self.lock:
            self.count -= 1
            if self.count < 0:
                print("Process is waiting...")
                # Use self.lock.wait() to block the thread, instead of output_queue.get()
                self.lock.wait()
    #The V method represents the "V" operation of the semaphore,
    #It increases the count by 1.
    #If the count is less than or equal to 0,
    #it means that there are threads waiting for a resource,
    #so self.lock.notify() is called to wake up one waiting thread.
    def V(self):
        with self.lock:
            self.count += 1
            if self.count <= 0:
                self.lock.notify()
                

def process(process_id):
    # output_queue.put(f"Process {process_id} is trying to access the resource...")
    # semaphore.P()
    # output_queue.put(f"Process {process_id} has accessed the resource.")
    # # Simulating some work being done by the process
    # output_queue.put(f"Process {process_id} is performing some work...")
    # output_queue.put(f"Process {process_id} has completed its work.")
    # semaphore.V()
    # output_queue.put(f"Process {process_id} has released the resource.")


    print(f"Process {process_id} is trying to access the resource...")
    semaphore.P()
    print(f"Process {process_id} has accessed the resource.")
    # Simulating some work being done by the process
    print(f"Process {process_id} is performing some work...")
    print(f"Process {process_id} has completed its work.")
    semaphore.V()
    print(f"Process {process_id} has released the resource.")



def add_process():
    process_name = entry.get()
    if process_name:
        added_processes.append(process_name)
        process_list.insert(tk.END, process_name)
        entry.delete(0, tk.END)


def start_simulation():
    for process_name in added_processes:
        process_thread = threading.Thread(target=process, args=(process_name,))
        process_thread.start()


def update_output_text():
    while not output_queue.empty():
        output_text.insert(tk.END, output_queue.get() + "\n")
    output_text.after(100, update_output_text)


# Create the main window
window = tk.Tk()
window.title("Semaphore Simulation")
window.geometry("400x400")

# Create an entry field for adding processes
label = tk.Label(window, text="Enter process name")
label.pack(pady=1)

# Create an entry field for adding processes
entry = tk.Entry(window)
entry.pack(pady=6)

# Create the "Add" button
add_button = tk.Button(window, text="Add", command=add_process)
add_button.pack(pady=6)

# Create the process list box
process_list = tk.Listbox(window)
process_list.pack(pady=6)


# Create the "Start" button
start_button = tk.Button(window, text="Start", command=start_simulation)
start_button.pack(pady=6)

# Create a text widget to display the output
output_text = tk.Text(window, width=2, height=2)
output_text.pack(pady=6)

# Create a thread-safe queue to capture the output
output_queue = queue.Queue()

# Start updating the output_text periodically
update_output_text()

# Create a semaphore with an initial count of 1
semaphore = Semaphore(1)

# List to store the added processes
added_processes = []

# Start the GUI event loop
window.mainloop()
