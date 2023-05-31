from threading import Thread, Lock
import time
import tkinter as tk


class ReaderWriterLock:
    def __init__(self):
        self.mutex = Lock()  # Semaphore for mutual exclusion when updating readcnt
        self.wrt = Lock()  # Semaphore for writers
        self.readcnt = 0  # Number of readers in the critical section

    def acquire_read(self):
        self.mutex.acquire()
        self.readcnt += 1
        if self.readcnt == 1:
            self.wrt.acquire()
        self.mutex.release()

    def release_read(self):
        self.mutex.acquire()
        self.readcnt -= 1
        if self.readcnt == 0:
            self.wrt.release()
        self.mutex.release()

    def acquire_write(self):
        self.wrt.acquire()

    def release_write(self):
        self.wrt.release()


def reader(lock, id, text_widget):
    for _ in range(2):
        lock.acquire_read()
        text_widget.insert(tk.END, f"{time.strftime('%H:%M:%S')} Reader {id} is reading the resource\n")
        text_widget.see(tk.END)
        time.sleep(1)
        text_widget.insert(tk.END, f"{time.strftime('%H:%M:%S')} Reader {id} has finished reading\n")
        text_widget.see(tk.END)
        lock.release_read()
        time.sleep(1)


def writer(lock, id, text_widget):
    for _ in range(2):
        lock.acquire_write()
        text_widget.insert(tk.END, f"{time.strftime('%H:%M:%S')} Writer {id} is waiting for the lock\n")
        text_widget.see(tk.END)
        time.sleep(1)
        text_widget.insert(tk.END, f"{time.strftime('%H:%M:%S')} Writer {id} is writing to the resource\n")
        text_widget.see(tk.END)
        time.sleep(1)
        text_widget.insert(tk.END, f"{time.strftime('%H:%M:%S')} Writer {id} has finished writing\n")
        text_widget.see(tk.END)
        lock.release_write()
        time.sleep(1)


reader_threads = []
writer_threads = []


def start_threads():
    global reader_threads, writer_threads

    num_readers = int(reader_entry.get())
    num_writers = int(writer_entry.get())

    lock = ReaderWriterLock()

    # Clear the text widget
    text_widget.delete('1.0', tk.END)

    # Create reader threads
    reader_threads = []
    for i in range(num_readers):
        reader_thread = Thread(target=reader, args=(lock, i + 1, text_widget))
        reader_threads.append(reader_thread)

    # Create writer threads
    writer_threads = []
    for i in range(num_writers):
        writer_thread = Thread(target=writer, args=(lock, i + 1, text_widget))
        writer_threads.append(writer_thread)

    # Start reader threads
    for thread in reader_threads:
        thread.start()

    # Start writer threads
    for thread in writer_threads:
        thread.start()


# Create a Tkinter GUI window
window = tk.Tk()
window.title("Reader-Writer Lock Example")

# Create labels and entry fields for readers and writers
reader_label = tk.Label(window, text="Number of Readers:")
reader_label.pack(pady=10)
reader_entry = tk.Entry(window)
reader_entry.pack()

writer_label = tk.Label(window, text="Number of Writers:")
writer_label.pack(pady=10)
writer_entry = tk.Entry(window)
writer_entry.pack()

# Create a button to start the threads
start_button = tk.Button(window, text="Start", command=start_threads)
start_button.pack(pady=10)

# Create a text widget to display the output
text_widget = tk.Text(window, height=10, width=50)
text_widget.pack(pady=10)


def close_window():
    # Function to be called when the window is closed
    # Terminate all threads
    for thread in reader_threads + writer_threads:
        thread.join()
    window.destroy()


# Set the close_window function as the close event handler
window.protocol("WM_DELETE_WINDOW", close_window)

# Start the Tkinter event loop
window.mainloop()