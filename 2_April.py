# =====================================================
# Write a program to check no is odd or even 
 
def oddeven(a):
    if a%2 == 0:
        print("It's Even...")
    else:
        print("It's Odd...")

# =====================================================
# Write a program to check prime no
               
def prime(n):
    flag = True
    if n == 1 or n == 0:
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
# Write a program to check no is palindrome or not
            
# Solution : 1
        
# def palindrome(str1):
#     if str(str1) == str(str1)[::-1] :
#         print("Palindrome...")
#     else:
#         print("Not a Palindrome..")

# Solution 2
        
# def palindrome(str1): 
#     reversed = ''
    
#     if len(str1) <= 0:
#         return False
#     for i in str1:
#         reversed = i + reversed
#     # print(reversed)
#     return str1 == reversed
        
# Solution 3
        
def palindrome(s):
    i, j = 0, len(s) - 1 # Assigning Initial Values to i,j

    while i < j:
        if s[i] != s[j]:
            return False # Not a Palindrome
        i = i + 1
        j = j - 1
    
    return True # It's a Palindrome

# =====================================================

# Write a program  statement to check if a number is positive, negative, or zero 

def check_number(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")
     
# =====================================================


def main():
    # num = int(input("enter your number : "))
    # ==============================================
    # oddeven(num)
    # ==============================================
    # prime(num)
    # ==============================================
    str1 = input("Enter Input : ")
    if palindrome(str1):
        print("Palindrome")
    else:
        print("Not Palindrome")
    # ==============================================
    # check_number(num)
if __name__ == "__main__":
    main()
