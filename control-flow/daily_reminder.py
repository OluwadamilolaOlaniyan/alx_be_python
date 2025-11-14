task =input("Enter your task: ")
priority =input("Priority (high/medium/low): ")
time_bound =input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' is a task with unspecified priority"               


if time_bound == "yes":
    final_message = f"Reminder: {base_message} that requires immediate attention today!"
else:
    final_message = f"Reminder: Note: {base_message}. Consider completing it when you have free time."


print(final_message)