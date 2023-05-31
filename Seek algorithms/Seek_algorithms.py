import tkinter as tk


root = tk.Tk()
root.geometry("600x700")
root.title("Graph")

def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# Create a vertical scrollbar
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas_width = 550
canvas_height = 4000
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.TOP, fill=tk.BOTH)
scrollbar.config(command=canvas.yview)

# Bind the mousewheel event to the canvas for scrolling
canvas.bind_all("<MouseWheel>", on_mousewheel)

counter = 1

######################################################################################################
def FCFS(requests_queue, head_pos):
    
    global counter
    total_seek_time = 0
    output = ""

    drawn_request = requests_queue.copy()
    drawn_request.append(head_pos)
    drawn_request.sort()

    spacing = canvas_width / (len(drawn_request) + 1)  # Calculate the spacing between requests

    counter = 1
    # Draw the requests
    for i, track in enumerate(drawn_request):
        x = (i + 1) * spacing  # Calculate the x-coordinate position with spacing
        if track == head_pos:
            head_x = x
        canvas.create_text(x, 50, text=str(track), anchor="center")

    for req in requests_queue:
        seek_time = abs(req - head_pos)
        output += f"Move from {head_pos} to {req} - Seek Time: {seek_time}\n"
        total_seek_time += seek_time

        # Draw a diagonal line from head to request 25
        y_coordinate = 80 + counter
        x_coordinate = 70 + counter
        target_track = req
        if target_track in requests_queue:
            target_x = (drawn_request.index(target_track) + 1) * spacing
            canvas.create_line(head_x, x_coordinate, target_x, y_coordinate, fill="red")

            # Draw a point at the end of the line
            point_size = 4
            canvas.create_oval(target_x - point_size, y_coordinate - point_size, target_x + point_size, y_coordinate + point_size, fill="green")

        head_x = target_x

        head_pos = req
        counter += 10
    
    canvas.create_line(0, counter+110, canvas_width, counter+110, fill="black")
    return total_seek_time, output

########################################################################################################

def SSTF(requests_queue, head_pos):
    
    global counter
    total_seek_time = 0
    temp_queue = requests_queue.copy()
    output = ""

    drawn_request = requests_queue.copy()
    drawn_request.append(head_pos)
    drawn_request.sort()

    spacing = canvas_width / (len(drawn_request) + 1)  # Calculate the spacing between requests


    # Draw the requests
    H = 140 + counter
    for i, track in enumerate(drawn_request):
        x = (i + 1) * spacing  # Calculate the x-coordinate position with spacing
        if track == head_pos:
            head_x = x
        canvas.create_text(x, H, text=str(track), anchor="center")

    while temp_queue:
        shortest = min(temp_queue, key=lambda x: abs(head_pos - x))
        seek_time = abs(shortest - head_pos)
        output += f"Move from {head_pos} to {shortest} - Seek Time: {seek_time}\n"
        total_seek_time += seek_time

        # Draw a diagonal line from head to request 25
        y_coordinate = 180 + counter
        x_coordinate = 170 + counter
        target_track = shortest
        if target_track in requests_queue:
            target_x = (drawn_request.index(target_track) + 1) * spacing
            canvas.create_line(head_x, x_coordinate, target_x, y_coordinate, fill="red")

            # Draw a point at the end of the line
            point_size = 4
            canvas.create_oval(target_x - point_size, y_coordinate - point_size, target_x + point_size, y_coordinate + point_size, fill="green")

        head_x = target_x

        head_pos = shortest
        temp_queue.remove(shortest)
        counter += 10

    canvas.create_line(0, counter+210, canvas_width, counter+210, fill="black")
    return total_seek_time, output


############################################################################################

def SCAN(requests_queue, head):

    global counter
	
    max_size = max(requests_queue) + 20
    output = ""

    requests_queue.append(0)  # Add the boundary track at the beginning
    requests_queue.append(max_size)  # Add the boundary track at the end
    requests_queue.append(head)

    spacing = canvas_width / (len(requests_queue) + 1)  # Calculate the spacing between requests

    drawn_request = requests_queue.copy()
    drawn_request.sort()

    # Draw the requests
    H = 240 + counter
    for i, track in enumerate(drawn_request):
        x = (i + 1) * spacing  # Calculate the x-coordinate position with spacing
        if track == head:
            head_x = x
        canvas.create_text(x, H, text=str(track), anchor="center")

    
    total_seek_time = 0
    distance = 0
    cur_request = 0

    left = []
    right = []

    
	# Tracks on the left of the
	# head will be serviced when
	# once the head comes back
	# to the beginning (left end)
    for i in range(len(requests_queue)):
        if (requests_queue[i] < head):
            left.append(requests_queue[i])
        if (requests_queue[i] >= head):
            right.append(requests_queue[i])

	# Sorting left and right vectors
    left.sort(reverse=True)
    right.sort()


	# go through the right side
    for i in range(1, len(right)):
        cur_request = right[i]
		

		# Calculate absolute distance
        distance = abs(cur_request - head)
        output += f"Move from {head} to {cur_request} - Seek Time: {distance}\n"

		# Increase the total count
        total_seek_time += distance

        # Draw a diagonal line from head to request 25
        y_coordinate = 280 + counter
        x_coordinate = 270 + counter
        target_track = cur_request
        if target_track in requests_queue:
            target_x = (drawn_request.index(target_track) + 1) * spacing
            canvas.create_line(head_x, x_coordinate, target_x, y_coordinate, fill="red")

            # Draw a point at the end of the line
            point_size = 4
            canvas.create_oval(target_x - point_size, y_coordinate - point_size, target_x + point_size, y_coordinate + point_size, fill="green")

        head_x = target_x

		# Accessed track is now new head
        head = cur_request
        counter += 10

	# left side now
    for i in range(len(left)):
        cur_request = left[i]

		# Calculate absolute distance
        distance = abs(cur_request - head)
        output += f"Move from {head} to {cur_request} - Seek Time: {distance}\n"

		# Increase the total count
        total_seek_time += distance

        # Draw a diagonal line from head to request 25
        y_coordinate = 280 + counter
        x_coordinate = 270 + counter
        target_track = cur_request
        if target_track in requests_queue:
            target_x = (drawn_request.index(target_track) + 1) * spacing
            canvas.create_line(head_x, x_coordinate, target_x, y_coordinate, fill="red")

            # Draw a point at the end of the line
            point_size = 4
            canvas.create_oval(target_x - point_size, y_coordinate - point_size, target_x + point_size, y_coordinate + point_size, fill="green")

        head_x = target_x

		# Accessed track is now the new head
        head = cur_request
        counter += 10

    canvas.create_line(0, counter+310, canvas_width, counter+310, fill="black")
    return total_seek_time, output
##################################################################################################

def LOOK(requests_queue, head):

    global counter
	
    output = ""
    
    requests_queue.append(head)

    spacing = canvas_width / (len(requests_queue) + 1)  # Calculate the spacing between requests

    drawn_request = requests_queue.copy()
    drawn_request.sort()

    # Draw the requests
    H = 340 + counter
    for i, track in enumerate(drawn_request):
        x = (i + 1) * spacing  # Calculate the x-coordinate position with spacing
        if track == head:
            head_x = x
        canvas.create_text(x, H, text=str(track), anchor="center")

    
    total_seek_time = 0
    distance = 0
    cur_request = 0

    left = []
    right = []

    
	# Tracks on the left of the
	# head will be serviced when
	# once the head comes back
	# to the beginning (left end)
    for i in range(len(requests_queue)):
        if (requests_queue[i] < head):
            left.append(requests_queue[i])
        if (requests_queue[i] >= head):
            right.append(requests_queue[i])

	# Sorting left and right vectors
    left.sort(reverse=True)
    right.sort()


	# go through the right side
    for i in range(1, len(right)):
        cur_request = right[i]
		

        distance = abs(cur_request - head)
        output += f"Move from {head} to {cur_request} - Seek Time: {distance}\n"

        total_seek_time += distance

        # Draw a diagonal line from head to request 25
        y_coordinate = 370 + counter
        x_coordinate = 360 + counter
        target_track = cur_request
        if target_track in requests_queue:
            target_x = (drawn_request.index(target_track) + 1) * spacing
            canvas.create_line(head_x, x_coordinate, target_x, y_coordinate, fill="red")

            # Draw a point at the end of the line
            point_size = 4
            canvas.create_oval(target_x - point_size, y_coordinate - point_size, target_x + point_size, y_coordinate + point_size, fill="green")

        head_x = target_x

        head = cur_request
        counter += 10

	# right side finished   
    
    # output += f"Move from {head} to {left[0]} - \n"
    # head = left[0]
    
	# left side now
    for i in range(len(left)):
        cur_request = left[i]

        distance = abs(cur_request - head)
        output += f"Move from {head} to {cur_request} - Seek Time: {distance}\n"

        total_seek_time += distance

        # Draw a diagonal line from head to request 25
        y_coordinate = 370 + counter
        x_coordinate = 360 + counter
        target_track = cur_request
        if target_track in requests_queue:
            target_x = (drawn_request.index(target_track) + 1) * spacing
            canvas.create_line(head_x, x_coordinate, target_x, y_coordinate, fill="red")

            # Draw a point at the end of the line
            point_size = 4
            canvas.create_oval(target_x - point_size, y_coordinate - point_size, target_x + point_size, y_coordinate + point_size, fill="green")

        head_x = target_x

        head = cur_request
        counter += 10
    
    canvas.create_line(0, counter+410, canvas_width, counter+410, fill="black")
    return total_seek_time, output
###############################################################################################################

def CSCAN(requests_queue, head):
    #direction here is right by the default

    global counter
	
    max_size = max(requests_queue) + 20
    output = ""

    requests_queue.append(0)  # Add the boundary track at the beginning
    requests_queue.append(max_size)  # Add the boundary track at the end
    requests_queue.append(head)

    spacing = canvas_width / (len(requests_queue) + 1)  # Calculate the spacing between requests

    drawn_request = requests_queue.copy()
    drawn_request.sort()

    # Draw the requests
    H = 440 + counter
    for i, track in enumerate(drawn_request):
        x = (i + 1) * spacing  # Calculate the x-coordinate position with spacing
        if track == head:
            head_x = x
        canvas.create_text(x, H, text=str(track), anchor="center")
    
    total_seek_time = 0
    distance = 0
    cur_request = 0

    left = []
    right = []

    
	# Tracks on the left of the
	# head will be serviced when
	# once the head comes back
	# to the beginning (left end)
    for i in range(len(requests_queue)):
        if (requests_queue[i] < head):
            left.append(requests_queue[i])
        if (requests_queue[i] >= head):
            right.append(requests_queue[i])

	# Sorting left and right vectors
    left.sort()
    right.sort()

	# go through the right side
    for i in range(1, len(right)):
        cur_request = right[i]
		

        distance = abs(cur_request - head)
        output += f"Move from {head} to {cur_request} - Seek Time: {distance}\n"

        total_seek_time += distance

        # Draw a diagonal line from head to request 25
        y_coordinate = 480 + counter
        x_coordinate = 470 + counter
        target_track = cur_request
        if target_track in requests_queue:
            target_x = (drawn_request.index(target_track) + 1) * spacing
            canvas.create_line(head_x, x_coordinate, target_x, y_coordinate, fill="red")

            # Draw a point at the end of the line
            point_size = 4
            canvas.create_oval(target_x - point_size, y_coordinate - point_size, target_x + point_size, y_coordinate + point_size, fill="green")

        head_x = target_x

        head = cur_request
        counter += 10

	# right side finished   
    
    output += f"Move from {head} to {left[0]} - \n"
    head = left[0]
    target_x = (drawn_request.index(left[0]) + 1) * spacing
    canvas.create_line(head_x, 470 + counter, target_x, 480 + counter, fill="red")
    canvas.create_oval(target_x - 4, 480 + counter - 4, target_x + 4, 480 + counter + 4, fill="green")
    head_x = target_x
    counter += 10
    
	# left side now
    for i in range(1, len(left)):
        cur_request = left[i]

        distance = abs(cur_request - head)
        output += f"Move from {head} to {cur_request} - Seek Time: {distance}\n"

        total_seek_time += distance

        # Draw a diagonal line from head to request 25
        y_coordinate = 480 + counter
        x_coordinate = 470 + counter
        target_track = cur_request
        if target_track in requests_queue:
            target_x = (drawn_request.index(target_track) + 1) * spacing
            canvas.create_line(head_x, x_coordinate, target_x, y_coordinate, fill="red")

            # Draw a point at the end of the line
            point_size = 4
            canvas.create_oval(target_x - point_size, y_coordinate - point_size, target_x + point_size, y_coordinate + point_size, fill="green")

        head_x = target_x

        head = cur_request
        counter += 10
    
    canvas.create_line(0, counter+510, canvas_width, counter+510, fill="black")
    return total_seek_time, output
#####################################################################################################3

def CLOOK(requests_queue, head):	

    global counter
	
    output = ""
    
    requests_queue.append(head)

    spacing = canvas_width / (len(requests_queue) + 1)  # Calculate the spacing between requests

    drawn_request = requests_queue.copy()
    drawn_request.sort()

    # Draw the requests
    H = 540 + counter
    for i, track in enumerate(drawn_request):
        x = (i + 1) * spacing  # Calculate the x-coordinate position with spacing
        if track == head:
            head_x = x
        canvas.create_text(x, H, text=str(track), anchor="center")


    total_seek_time = 0
    distance = 0
    cur_request = 0

    left = []
    right = []

    
	# Tracks on the left of the
	# head will be serviced when
	# once the head comes back
	# to the beginning (left end)
    for i in range(len(requests_queue)):
        if (requests_queue[i] < head):
            left.append(requests_queue[i])
        if (requests_queue[i] >= head):
            right.append(requests_queue[i])

	# Sorting left and right vectors
    left.sort()
    right.sort()

	# go through the right side
    for i in range(1, len(right)):
        cur_request = right[i]
		

        distance = abs(cur_request - head)
        output += f"Move from {head} to {cur_request} - Seek Time: {distance}\n"

        total_seek_time += distance

        # Draw a diagonal line from head to request 25
        y_coordinate = 580 + counter
        x_coordinate = 570 + counter
        target_track = cur_request
        if target_track in requests_queue:
            target_x = (drawn_request.index(target_track) + 1) * spacing
            canvas.create_line(head_x, x_coordinate, target_x, y_coordinate, fill="red")

            # Draw a point at the end of the line
            point_size = 4
            canvas.create_oval(target_x - point_size, y_coordinate - point_size, target_x + point_size, y_coordinate + point_size, fill="green")

        head_x = target_x

		# Accessed track is now new head
        head = cur_request
        counter += 10

	# right side finished   
    
    output += f"Move from {head} to {left[0]} - \n"
    head = left[0]
    target_x = (drawn_request.index(left[0]) + 1) * spacing
    canvas.create_line(head_x, 580 + counter, target_x, 580 + counter, fill="red")
    canvas.create_oval(target_x - 4, 580 + counter - 4, target_x + 4, 580 + counter + 4, fill="green")
    head_x = target_x
    counter += 10
    
	# left side now
    for i in range(1, len(left)):
        cur_request = left[i]

        distance = abs(cur_request - head)
        output += f"Move from {head} to {cur_request} - Seek Time: {distance}\n"

        total_seek_time += distance

        # Draw a diagonal line from head to request 25
        y_coordinate = 580 + counter
        x_coordinate = 570 + counter
        target_track = cur_request
        if target_track in requests_queue:
            target_x = (drawn_request.index(target_track) + 1) * spacing
            canvas.create_line(head_x, x_coordinate, target_x, y_coordinate, fill="red")

            # Draw a point at the end of the line
            point_size = 4
            canvas.create_oval(target_x - point_size, y_coordinate - point_size, target_x + point_size, y_coordinate + point_size, fill="green")

        head_x = target_x

		# Accessed track is now the new head
        head = cur_request
        counter += 10

    canvas.create_line(0, counter+610, canvas_width, counter+610, fill="black")
    return total_seek_time, output

##############################################################################################

def add_to_sequence():
    value = seq_entry.get()
    if value.isdigit():
        sequence.append(int(value))
        seq_entry.delete(0, tk.END)
        sequence_box.config(text=sequence)
        print(f"Added {value} to the sequence.")
    else:
        print("Invalid input. Please enter a number.")


def calculate_seek_time():
    head = head_entry.get()
    if head.isdigit():
        head_pos = int(head)
        ans1, output1 = FCFS(sequence.copy(), head_pos)
        ans2, output2 = SSTF(sequence.copy(), head_pos)
        ans3, output3 = SCAN(sequence.copy(), head_pos)
        ans4, output4 = LOOK(sequence.copy(), head_pos)
        ans5, output5 = CSCAN(sequence.copy(), head_pos)
        ans6, output6 = CLOOK(sequence.copy(), head_pos)
        # output = f"\nFCFS seek time:\nTotal Seek time: {ans1}\n\n\n" \
        #          f"SSTF seek time:\nTotal Seek time: {ans2}\n\n" \
        #          f"SCAN seek time:\nTotal Seek time: {ans3}\n\n" \
        #          f"LOOK seek time:\nTotal Seek time: {ans4}"
        one = f"\nFCFS seek time: \n" \
            f"{output1}" \
            f"Total Seek time: {ans1}\n"
        two = f"\nSSTF seek time:\n" \
            f"{output2}" \
            f"Total Seek time: {ans2}\n"
        three = f"\nSCAN seek time:\n" \
            f"{output3}" \
            f"Total Seek time: {ans3}\n"
        four = f"\nLOOK seek time:\n" \
            f"{output4}" \
            f"Total Seek time: {ans4}\n"
        five = f"\nC-SCAN seek time:\n" \
            f"{output5}" \
            f"Total Seek time: {ans5}\n"
        six = f"\nC-LOOK seek time:\n" \
            f"{output6}" \
            f"Total Seek time: {ans6}\n"
        
        set_output_text(one + two + three + four + five + six)
        sequence.clear()
        seq_entry.delete(0, tk.END)
        head_entry.delete(0, tk.END)
        # sequence_box.config(text="")
    else:
        print("Invalid head position. Please enter a number.")
    root.mainloop()


def set_output_text(text):
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, text)


# Create a Tkinter window
window = tk.Tk()
window.title("Disk Scheduling Algorithm")
window.geometry("400x700")

# Create seq input label
seq_label = tk.Label(window, text="Enter a sequence:")
seq_label.pack()

# Create seq input field
seq_entry = tk.Entry(window, width=30)
seq_entry.pack()

# Create head input label
head_label = tk.Label(window, text="Enter head position:")
head_label.pack()

# Create head input field
head_entry = tk.Entry(window, width=10)
head_entry.pack()

# Create a list to store the sequence
sequence = []

# Create display seq label
display_seq_label = tk.Label(window, text="The Entered sequence:")
display_seq_label.pack()

# Create a box to display the entered sequence
sequence_box = tk.Label(window, text="", padx=5, pady=5, bg="lightblue", highlightbackground="black", highlightthickness=1)
sequence_box.pack()

# Create buttons
add_button = tk.Button(window, text="Add to Sequence", command=add_to_sequence)
add_button.pack(pady=5)

calculate_button = tk.Button(window, text="Calculate Seek Time", command=calculate_seek_time)
calculate_button.pack(pady=(5, 10))

# Create output scrollable frame
output_frame = tk.Frame(window)
output_frame.pack(fill=tk.BOTH, expand=True)

# Create a scrollbar
scrollbar = tk.Scrollbar(output_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create output text widget
output_text = tk.Text(output_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
output_text.pack(fill=tk.BOTH, expand=True)

# Configure the scrollbar
scrollbar.config(command=output_text.yview)

# Start the Tkinter event loop
window.mainloop()









# # Example usage
# requests_queue = [55, 12, 43, 36, 6, 25, 32]
# head = 20