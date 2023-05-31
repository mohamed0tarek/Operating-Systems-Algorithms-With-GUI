# Task Scheduling Tests

This directory contains implementations of task scheduling tests used to determine the schedulability of tasks. The following tests are implemented:

- Bound Test
- Completion Test

## How to Use

To run the task scheduling tests and determine the schedulability of tasks, follow these steps:

1. Ensure you have Python installed on your system.
2. Navigate to the root directory.
3. Open the `main.py` file.
4. From the main interface, choose the desired test.
5. In the user interface, enter the task information for each task, including arrival time, period time, execution time, and deadline.
6. Click the "Add Task" button to add the task to the list.
7. Repeat step 5 for each task you want to add.
8. Click the "Run Test" button to execute the task scheduling test.
9. The output will display the schedulability result for each task, indicating whether the task is schedulable or not.

## Task Information

For each task, provide the following information:

- Arrival Time: The time at which the task arrives in the system.
- Period Time: The time interval between two consecutive arrivals of the task.
- Execution Time: The time required to complete the execution of the task.
- Deadline: The time by which the task must be completed.

## Output

The output of the task scheduling tests shows the schedulability result for each task. It will indicate whether each task is schedulable or not based on the selected test algorithm.

## Dependencies

The task scheduling tests are implemented using Python. Please ensure you have Python installed on your system.
