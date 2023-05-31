import sys
from tkinter import *
import os
from threading import Thread
import time

def FIFO():
    os.system('cd "Task scheduling algorithms" && python FIFO.py')

def open_FIFO():
    Thread(target = FIFO).start() 

def round_robin():
    os.system('cd "Task scheduling algorithms" && python round_robin.py')

def open_RR():
    Thread(target = round_robin).start() 

def Seek_algorithms():
    os.system('cd "Seek algorithms" && python Seek_algorithms.py')

def open_SA():
    Thread(target = Seek_algorithms).start() 

def DMA():
    os.system('cd "Task scheduling algorithms" && python DMA.py')

def open_DMA():
    Thread(target = DMA).start() 

def semaphores():
    os.system('cd semaphores && python semaphores.py')

def open_sema():
    Thread(target = semaphores).start() 

def RMA():
    os.system('cd "Task scheduling algorithms" && python RMA.py')

def open_RMA():
    Thread(target = RMA).start() 

def EDF():
    os.system('cd "Task scheduling algorithms" && python EDF.py')

def open_EDF():
    Thread(target = EDF).start() 

def bound():
    os.system('cd "Task scheduling tests" && python bound_test.py')

def open_bound():
    Thread(target = bound).start() 

def RW():
    os.system('cd semaphores && python Read_Write.py')

def open_RW():
    Thread(target = RW).start()

def completion():
    os.system('cd "Task scheduling tests" && python completion_test.py')

def open_completion():
    Thread(target = completion).start()

color1 = "#f1f1f2"
color2 = "#fa6e59"
color3 = "#ffdb5c"
color4 = "#5EA9E8"
color5 = "#5EEAB0"
# Create the main window
window = Tk()
window.title("ALL ALGORITHMS")
window.geometry("850x600")
window.config(bg=color1)

# semaphores Scheduler button
scheduler_button = Button(window, text="Run semaphores",padx=10, pady=10, bd=3, bg=color2, font = ('', 12), command=open_sema)
scheduler_button.grid(row=1, column= 3, pady=10, padx=40)
# scheduler_button.pack(pady=10)

# Read Write button
scheduler_button = Button(window, text="Run Readers & Writers",padx=10, pady=10, bd=3, bg=color2, font = ('', 12), command=open_RW)
scheduler_button.grid(row=2, column= 3, pady=10, padx=40)
# scheduler_button.pack(pady=10)

# Seek_algorithms Scheduler button
scheduler_button = Button(window, text="Run Seek algorithms",padx=10, pady=10, bd=3, bg=color3, font = ('', 12), command=open_SA)
scheduler_button.grid(row=3, column= 3, pady=30, padx=40)
# scheduler_button.pack(pady=10)

# FIFO Scheduler button
scheduler_button = Button(window, text="Run FIFO Scheduler",padx=10, pady=10, bd=3, bg=color4, font = ('', 12), command=open_FIFO)
scheduler_button.grid(row=1, column= 6, pady=30, padx=60)
# scheduler_button.pack(pady=10)

# RR Scheduler button
scheduler_button = Button(window, text="Run RR Scheduler",padx=10, pady=10, bd=3, bg=color4, font = ('', 12), command=open_RR)
scheduler_button.grid(row=2, column= 6, pady=30, padx=60)
# scheduler_button.pack(pady=10)

# DMA Scheduler button
scheduler_button = Button(window, text="Run DMA Scheduler",padx=10, pady=10, bd=3, bg=color4, font = ('', 12), command=open_DMA)
scheduler_button.grid(row=3, column= 6, pady=30, padx=60)
# scheduler_button.pack(pady=10)

# RMA Scheduler button
scheduler_button = Button(window, text="Run RMA Scheduler",padx=10, pady=10, bd=3, bg=color4, font = ('', 12), command=open_RMA)
scheduler_button.grid(row=4, column= 6, pady=30, padx=60)
# scheduler_button.pack(pady=10)

# EDF Scheduler button
scheduler_button = Button(window, text="Run EDF Scheduler",padx=10, pady=10, bd=3, bg=color4, font = ('', 12), command=open_EDF)
scheduler_button.grid(row=5, column= 6, pady=30, padx=60)
# scheduler_button.pack(pady=10)

# Bound Test button
scheduler_button = Button(window, text="Run Bound Test",padx=10, pady=10, bd=3, bg=color5, font = ('', 12), command=open_bound)
scheduler_button.grid(row=1, column= 8, pady=30, padx=40)
# scheduler_button.pack(pady=10)

# completion Test button
scheduler_button = Button(window, text="Run completion Test",padx=10, pady=10, bd=3, bg=color5, font = ('', 12), command=open_completion)
scheduler_button.grid(row=2, column= 8, pady=30, padx=40)
# scheduler_button.pack(pady=10)

# Start the main loop
window.mainloop()

