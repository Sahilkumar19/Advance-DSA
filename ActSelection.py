"""
Acivity selection problem
Author : Sahil Kumar
Date : 4/03/2024
"""
def activity_selection_left_to_right(start_times, finish_times):
	"""
	"""
	# Handle empty inputs
	if not start_times or not finish_times:
		return 0

	# Sort activities by their finish times in ascending order
	activities = sorted(zip(start_times, finish_times), key=lambda activity: activity[1])

	selected_activities = []
	current_end_time = float('-inf')  # Use -inf for handling empty activities

	for start_time, end_time in activities:
        # Select activity only if its start time is after the previous activity's end time
		if start_time >= current_end_time:
			selected_activities.append((start_time, end_time))
			current_end_time = end_time
			print("Selected Activity:", (start_time, end_time))
	return len(selected_activities)


def activity_selection_right_to_left(start_times, finish_times):
	"""
	"""
	if not start_times or not finish_times:  # Handling empty inputs
		return 0

    # Sorted activities by their start times in descending order
	activities = sorted(zip(start_times, finish_times), key=lambda activity: activity[0], reverse=True)

	selected_activities = []
	current_start_time = float('inf')  # Used inf for handling empty activities

	for start_time, end_time in activities:
        # Select activity only if its end time is before the previous activity's start time
		if end_time <= current_start_time:
			selected_activities.append((start_time, end_time))
			current_start_time = start_time
			print("Selected Activity:", (start_time, end_time))

	return len(selected_activities)



start_times = [0, 3, 1, 5, 5, 8]
finish_times = [6, 4, 2, 9, 7, 9]

max_activities_left_to_right = activity_selection_left_to_right(start_times, finish_times)
print(f"Maximum activities (Left-to-Right): {max_activities_left_to_right}")
max_activities_right_to_left = activity_selection_right_to_left(start_times.copy(), finish_times.copy())  # Used copy to avoid side effects
print(f"Maximum activities (Right-to-Left): {max_activities_right_to_left}")






