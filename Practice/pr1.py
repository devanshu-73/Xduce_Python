def prime(n):
    flag = True
    if n<= 1:
        print('Not a Prime...')
    elif n>=2:
        for i in range(2,n):
            if n%2 == 0:
                flag = False
        if flag:
            print('Prime')
        else:
            print('Not a Prime')
        
def main():
    n = int(input('Enter Num : '))
    prime(n)


if __name__ == '__main__':
    main()