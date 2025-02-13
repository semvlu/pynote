res = ''
choice = ''
msg = ''
while choice != 0:
    choice = input("Do you want to encrypt or decrypt the message?\n 1: encrypt, 2: decrypt, 0 exit. ")
    if choice == '1':
        msg = input('\nEnter message for enc: ')
        for i in range(0, len(msg)):
            res = res + chr(ord(msg[i]) - 1)
        print(res)
        res = ''
    if choice == '2':
        msg = input('\nEnter message to dec: ')
        for i in range(0, len(msg)):
            res = res + chr(ord(msg[i]) + 1)
        print(res)
        res = ''
    elif choice != '0':
        print('You have entered an invalid input, please try again. \n\n')