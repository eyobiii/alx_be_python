
while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    if priority not in ["high", "medium", "low"]:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
        continue
    if time_bound not in ["yes", "no"]:
        print("Invalid input for time-bound. Please enter 'yes' or 'no'.")
        continue

   
    match priority:
        case "high":
            priority_msg = f"'{task}' is a high priority task"
        case "medium":
            priority_msg = f"'{task}' is a medium priority task"
        case "low":
            priority_msg = f"'{task}' is a low priority task"

   
    if time_bound == "yes":
        message = f"Reminder: {priority_msg} that requires immediate attention today!"
    else:
        message = f"Note: {priority_msg}. Consider completing it when you have free time."

    print("\n" + message)
    break
 


