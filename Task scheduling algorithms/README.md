# Task Scheduling Algorithms

This directory contains implementations of various task scheduling algorithms used in operating systems. The following task scheduling algorithms are implemented:

- FIFO (First-In, First-Out)
- Round Robin
- DMA (Deadline Monotonic Algorithm)
- RMA (Rate Monotonic Algorithm)
- EDF (Earliest Deadline First)

## How to Use

To run the task scheduling algorithms and visualize the timeline of tasks, follow these steps:

1. Ensure you have Python and Tkinter installed on your system.
2. Navigate to the root directory.
3. Open the `main.py` file.
4. From the main interface, choose the algoritm you desire.
5. In the user interface, enter the task information for each task, including arrival time, period time, execution time, and deadline.
6. Click the "Add Task" button to add the task to the list.
7. Repeat step 5 for each task you want to add.
8. Click the "Run" button to execute the task scheduling algorithm.
9. The output will be a graph that shows the timeline of all the tasks, indicating their execution and idle periods.

## Task Information

For each task, provide the following information:

- Arrival Time: The time at which the task arrives in the system.
- Period Time: The time interval between two consecutive arrivals of the task.
- Execution Time: The time required to complete the execution of the task.
- Deadline: The time by which the task must be completed.

## Output

The output of the task scheduling algorithms is a graph that visualizes the timeline of all the tasks. The graph shows the execution and idle periods of each task, providing insights into the scheduling of the tasks based on the selected algorithm.

## Dependencies

The task scheduling algorithms and GUI are implemented using Python with the Tkinter library for the graphical interface. Please ensure you have Tkinter installed, which is usually included with standard Python installations.
