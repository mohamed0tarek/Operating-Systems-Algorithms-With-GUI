# Seek Algorithms

This directory contains implementations of various disk scheduling algorithms used in operating systems. The following seek algorithms are implemented:

- FCFS (First-Come, First-Served)
- SSTF (Shortest Seek Time First)
- SCAN
- LOOK
- C-SCAN (Circular SCAN)
- C-LOOK (Circular LOOK)

## How to Use

To run the seek algorithms and visualize the head movements, follow these steps:

1. Ensure you have Python and Tkinter installed on your system.
2. Navigate to the root directory.
3. Open the `main.py` file.
4. In the main user interface, choose "Seek algorithms"
5. In the user interface, enter the disk access sequence and the initial head position.
6. Click the "Run" button to execute the algorithms.
7. The first window will display the head movements for each algorithm.
8. The second window will show graphs visualizing the head movements for each algorithm.

## Input Format

The input for the seek algorithms should be provided in the following format:

- Disk Access Sequence: Enter a sequence of track numbers separated by spaces or commas. For example: "10 5 7 12 2"
- Initial Head Position: Enter the initial head position as a single track number. For example: "8"

## Output

The output of the seek algorithms consists of two windows:

1. Head Movements: The first window shows the detailed head movements for each algorithm, including the track numbers visited and the direction of movement.
2. Graphs: The second window displays graphs that visualize the head movements for each algorithm. The graphs provide a visual representation of the seek time and the order in which tracks are accessed.

## Dependencies

The seek algorithms and GUI are implemented using Python with the Tkinter library for the graphical interface. Please ensure you have Tkinter installed, which is usually included with standard Python installations.
