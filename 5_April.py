# Todays Test:
# Suppose you are building a system to manage student grades. # Implement a Python program that includes the following functionalities:
# 1. A function to add a new student with their grades.
# 2. A function to calculate the average grade of a student.
# 3. A decorator function to ensure that only positive grades are accepted.
# 4. A function to retrieve the highest grade among all students.
# 5. A function to retrieve the average grade of all students.
# Constraints: - Use dictionaries to store student names as keys and their grades as values.


# to add a new student with their grades.
import logging


students = {}

def addStudent():
    check = int(input('Do u Want To Add Student[1/2] ? :'))
    
    if check == 1:

        #User Inputs
        while True:        
            name = input("Enter Student Name :")
            maths = input(f'Enter Maths Grade :')
            physics = input(f'Enter Physics Grade :')
            chemistry = input(f'Enter Chemistry Grade :')

            # Inserting inputs in Dictionary 
            students[name] = [maths,physics,chemistry] 
            print('Students : ',students)
            confirm = input('Do U Want to Add More Students[y/n] :')
            if confirm == 'n':
                break
            elif confirm == 'y':
                continue

    elif check == 2:
        pass

    def checkPositive(fun):
        pass
    @checkPositive
    def gradesPositive():
        pass

def avgGrade_Single_Student():
    pass

def highest_Grade():
    pass

def avgGrade_All_Student():
    pass


def main():
    print('''
            ************* Student Management System *************
                Choice 1 : Add Student || Postive Grade are Accepted Or Not
                Choice 2 : Avg Grade of Single Student
                Choice 3 : Avg Grade of All Student
                Choice 4 : Exit 
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
        print('SuccessFully Exited')
        exit()

if __name__ == '__main__':
    main()