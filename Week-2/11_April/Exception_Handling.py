# Exception Handling : Try Except

import logging

while True:
    try:    
        num1 = int(input("Enter Number 1: "))
        num2 = int(input("Enter Number 2: "))
        div1 = num1 / num2
        print("Answer:", div1)
        break
    except ValueError as e:
        logging.exception(e)
    except ZeroDivisionError as e:
        logging.exception(e)
    except Exception as e:
        logging.exception(e)
    else:
        print("No exceptions occurred.")
    finally: # Always runs exception occurs or not
        print("Finally Completed.....")
