# Program to calculate attendance percentage

# Accept input from user
total_working_days = int(input("Enter total number of working days: "))
days_absent = int(input("Enter total number of days absent: "))

# Calculate days attended
days_attended = total_working_days - days_absent

# Calculate attendance percentage
attendance_percentage = (days_attended / total_working_days) * 100

# Display percentage
print(f"\nAttendance Percentage: {attendance_percentage:.2f}%")

# Check eligibility
if attendance_percentage < 75:
    print("Student will NOT be allowed to sit in the exam.")
else:
    print("Student is allowed to sit in the exam.")