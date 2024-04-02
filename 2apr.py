# =====================================================
# Odd Even task
# a = int(input("Enter Number :"))


# if a%2 == 0:
#     print("It's Even...")
# else:
#     print("It's Odd...")

#using function
    
def oddeven(a):
    if a%2 == 0:
        print("It's Even...")
    else:
        print("It's Odd...")


# =====================================================
# Prime Number
        
def prime(n):
    flag = True
    if n == 1 and n == 0:
        print("Not a Prime")
    if n > 2:
        for i in range(2,n):
            if n%i == 0:
                flag = False
    if flag:
        print("no is prime")
    else:
        print("no is not prime")
        


# =====================================================

# Palindrome
        
# Solution : 1
def palindrome(str1):
    if str(str1) == str(str1)[::-1] :
        print("Palindrome...")
    else:
        print("Not a Palindrome..")



# =====================================================
        
# check if a number is positive, negative, or zero

def check_number(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")
     
# =====================================================



def main():
    num = int(input("enter your number : "))
    # ==============================================
    # oddeven(num)
    # ==============================================
    # prime(num)
    # ==============================================
    # str1 = input("Enter Something..")
    # palindrome(str1)
    # ==============================================
    check_number(num)
if __name__ == "__main__":
    main()
