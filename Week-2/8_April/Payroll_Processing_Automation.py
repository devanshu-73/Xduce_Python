import os
import shutil
import datetime

# Step 1: Check if current date is past 20th of the month
today = datetime.datetime.now()
if today.day <= 20:
    print("Payroll processing is scheduled after the 20th of the month.")
    exit()

# Step 2: Check if payroll.txt file is empty
payroll_folder = "Week-2//8_April//account"
file_name = "payroll.txt"

# Combine the current directory path with the folder name
folder_path = os.path.join(os.getcwd(), payroll_folder)

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

payroll_file_path = os.path.join(folder_path, file_name)

# Check if payroll file exists and is empty
if os.path.exists(payroll_file_path) and os.path.getsize(payroll_file_path) == 0:
    print("Payroll file is empty. No processing needed.")
    exit()

# Step 3: File Handling - Copy payroll file to work folder and rename
work_folder = "work/"
if not os.path.exists(work_folder):
    os.makedirs(work_folder)

payroll_file_name = os.path.basename(payroll_file_path)
new_file_name = today.strftime("%Y-%m-%d") + "_" + payroll_file_name
new_file_path = os.path.join(work_folder, new_file_name)

shutil.copy(payroll_file_path, new_file_path)
print(f"Payroll file copied to {work_folder} and renamed to {new_file_name}")

# Step 4: Process Payroll
payroll_data = []
with open(new_file_path, 'r') as file:
    for line in file:
        emp_code, work_days = line.strip().split(',')
        # Assuming base wage is fetched from employee data, calculation of salary happens here
        # For simplicity, let's assume base wage is 10 units per day
        salary = int(work_days) * 1000  
        payroll_data.append((emp_code, salary))

# Step 5: Obtain employee data from Excel file and add a salary column
employee_excel_path = "ActiveEmployeeData.xlsx"
employee_data = []
with open(employee_excel_path, 'r') as file:
    for line in file:
        emp_code, emp_name = line.strip().split(',')
        # Assuming base wage is fetched from employee data, calculation of salary happens here
        # For simplicity, let's assume base wage is 10 units per day
        salary = int(work_days) * 10
        employee_data.append((emp_code, emp_name, salary))

# Step 6: Generate Employee_salary_<date>.xlsx file
payroll_folder = "payroll/"
if not os.path.exists(payroll_folder):
    os.makedirs(payroll_folder)

output_file_name = f"Employee_salary_{today.strftime('%Y-%m-%d')}.xlsx"
output_file_path = os.path.join(payroll_folder, output_file_name)

# Write data to Excel file manually without using external libraries
with open(output_file_path, 'w') as output_file:
    output_file.write("Employee Code, Employee Name, Salary\n")
    for emp_code, _, salary in employee_data:
        output_file.write(f"{emp_code}, {emp_name}, {salary}\n")

print(f"Payroll processed successfully. Output file generated: {output_file_path}")

# Step 7: Copy output file to shared folder and delete from payroll folder
shared_folder = "shared/"
if not os.path.exists(shared_folder):
    os.makedirs(shared_folder)

shared_file_path = os.path.join(shared_folder, output_file_name)
shutil.copy(output_file_path, shared_file_path)
os.remove(output_file_path)

print(f"Output file copied to {shared_folder} and deleted from {payroll_folder}")

# Step 8: Handling not found employees
pending_folder = "pending/"
if not os.path.exists(pending_folder):
    os.makedirs(pending_folder)

# Check for any employees not found during processing and create a pending Excel file
not_found_employees = [emp_code for emp_code, _, _ in employee_data]
for emp_code, emp_name, _ in employee_data:
    if emp_code not in not_found_employees:
        pending_file_name = f"Pending_{today.strftime('%Y-%m-%d')}.xlsx"
        pending_file_path = os.path.join(pending_folder, pending_file_name)
        with open(pending_file_path, 'w') as pending_file:
            pending_file.write("Employee Code, Employee Name\n")
            pending_file.write(f"{emp_code}, {emp_name}\n")

print("Pending files created for employees not found during processing.")
