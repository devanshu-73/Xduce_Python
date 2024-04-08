# Todays Test Task:
# Suppose you are building a system to manage student grades. # Implement a Python program that includes the following functionalities:
# 1. A function to add a new student with their grades.
# 2. A function to calculate the average grade of a student.
# 3. A decorator function to ensure that Student is pass or fail in exam
# 4. A function to retrieve the highest grade among all students.
# 5. A function to retrieve the average grade of all students.
# Constraints: - Use dictionaries to store student names as keys and their 3 Subject grades as values.

students = {}

def checkpassfail(func):
    def wrapper():
        # User Inputs
        name = input("Enter Student Name: ")
        maths = int(input(f'Enter Maths Grade: '))
        physics = int(input(f'Enter Physics Grade: '))
        chemistry = int(input(f'Enter Chemistry Grade: '))

        if all(mark >= 0 for mark in [maths, physics, chemistry]):
            # Inserting inputs in Dictionary
            students[name] = {'Maths': maths, 'Physics': physics, 'Chemistry': chemistry}
            print('Students:', students)

            # Check pass/fail
            pass_fail = "Pass" if all(mark >= 5 for mark in [maths, physics, chemistry]) else "Fail"
            print(f"{name} You are {pass_fail} in Exams")
            func()

    return wrapper

@checkpassfail
def addStudent():
    while True:
        confirm = input('Do you want to add more students? [y/n]: ')
        if confirm == 'n':
            break
        elif confirm == 'y':
            addStudent()    
        else:
            break


def avgGrade_Single_Student():
    name = input("Enter Student Name: ")
    if name in students:
        total = sum(students[name].values())
        avg = total / 3
        print(f'{name} : Average Grade:', avg)
    else:
        print("Student not found.")

def highest_Grade():
    if students:
        highest_grade = 0
        highest_student = None
        for name, grades in students.items():
            max_grade = max(grades.values())
            if max_grade > highest_grade:
                highest_grade = max_grade
                highest_student = name
        if highest_student:
            print(f"Highest Grade among all students: {highest_grade} (Student: {highest_student})")
        else:
            print("No students found.")
    else:
        print("No students found.")


def avgGrade_All_Student():
    if students:
        total = sum(sum(student.values()) for student in students.values())
        num_students = len(students)
        avg = total / (num_students * 3)
        print("Average Grade of all students:", avg)
    else:
        print("No students found.")

def main():
    while True:
        print('''
                ************* Student Management System *************
                    Choice 1 : Add Student || Student Pass or Fail Checking (Decorator)
                    Choice 2 : Avg Grade of Single Student
                    Choice 3 : Highest Among All Students
                    Choice 4 : Avg Grade of All Student
                    Choice 5 : Exit 
        ''')
        ch = int(input('Enter Your Choice :'))

        if ch == 1:
            addStudent()
        elif ch == 2:
            avgGrade_Single_Student()
        elif ch == 3:
            highest_Grade()
        elif ch == 4:
            avgGrade_All_Student()
        elif ch == 5:
            print('Successfully Exited')
            break
        else:
            print("Invalid Choice. Please choose again.")

if __name__ == '__main__':
    main()
