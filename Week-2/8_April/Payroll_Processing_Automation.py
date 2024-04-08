import os
import datetime
import shutil
from openpyxl import load_workbook

# Function to check if current date is past 20th of the month
def past_20th():
    today = datetime.datetime.now()
    return today.day <= 20

# Function to check if payroll file is empty
def payroll_empty(file_path):
    return os.path.exists(file_path) and os.path.getsize(file_path) == 0

# Function to copy file from source folder to destination folder
def copy_file(source_path, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    file_name = os.path.basename(source_path)
    dest_path = os.path.join(dest_folder, file_name)

    with open(source_path, 'r') as src, open(dest_path, 'w') as dst:
        dst.write(src.read())

    print(f"File copied to {dest_folder}.")

    return dest_path

# Function to process payroll and generate Excel file
def process_payroll(payroll_file_path, employee_data_path):
    # print("==============================",payroll_file_path, employee_data_path)
    # Read payroll data and calculate salary
    payroll_data = {}
    with open(payroll_file_path, 'r') as file:
        for line in file:
            emp_code, work_days = line.strip().split(',')

            # print("Employee code:", emp_code)
            # print("Work days:", work_days)

            salary = int(work_days) * 1000
            payroll_data[emp_code] = salary

    # Read employee data and create a workbook
    wb = load_workbook(filename = 'ActiveEmployeeData.xlsx')
    sh1 = wb['Sheet1']

    rows = sh1.max_row  # inbuilt function
    columns = sh1.max_column # inbuilt function
    
    for c in range(1,columns+1):
        for r in range(1,rows+1):
            print()
    print('==============================================','rows :',rows,'columns :',columns)
    # print("============================================",sh1['G1'].value)
    pass

# Main function
def main():
    if not past_20th():
        print("Payroll processing is scheduled after the 20th of the month.")
        return

    payroll_file_path = "account/payroll.txt"
    employee_data_path = "ActiveEmployeeData.xlsx"
    shared_folder = "shared/"

    if payroll_empty(payroll_file_path):
        print("Payroll file is empty. No processing needed.")

    work_folder = "work/"
    new_file_path = copy_file(payroll_file_path, work_folder)

    output_file_path = process_payroll(new_file_path, employee_data_path)

    # Copy output file to shared folder and delete from payroll folder
    if not os.path.exists(shared_folder):
        os.makedirs(shared_folder)

    shared_file_path = os.path.join(shared_folder, os.path.basename(output_file_path))

    try:
        shutil.copy(output_file_path, shared_file_path)
        os.remove(output_file_path)
        print(f"Output file copied to {shared_folder} and deleted from payroll folder.")
    except Exception as e:
        print(f"Error occurred while copying/deleting file: {e}")

if __name__ == "__main__":
    main()

