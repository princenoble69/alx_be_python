task = input("Enter your task: ")

valid_priorities = ["high", "medium", "low"]
priority = ""

while priority not in valid_priorities:
    priority = input("Priority (high/medium/low): ").lower()
    if priority not in valid_priorities:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

time_bound = input("Is it time-bound? (yes/no): ").lower()

base_message = ""
time_sensitive_message = ""

match priority:
    case "high":
        base_message = f"'{task}' is a **{priority.upper()}** priority task."
    case "medium":
        base_message = f"'{task}' is a {priority} priority task. It's important, but flexible."
    case "low":
        base_message = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."
    case _:
        base_message = f"'{task}' has an unclassified priority."

if time_bound == "yes":
    time_sensitive_message = " that requires immediate attention today!"
elif time_bound == "no":
    time_sensitive_message = ""
else:
    time_sensitive_message = " (Please verify if this task is truly time-bound.)"

print("\n--- Task Reminder ---")
final_reminder = base_message + time_sensitive_message

print(f"Reminder: {final_reminder}")
print("---------------------")
