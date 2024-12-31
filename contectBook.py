# empty dictionary
contacts = {}

print("-----WELCOM TO THE CONTACT MANAGMENT SYSTEM-----")

while True:
    print('\n contact book app')
    print('1. create contact')
    print('2. view   contact')
    print('3. update contact')
    print('4. delete contact')
    print('5. search contact')
    print('6. count  contact')
    print('7. exit')
    # All opretiopn are prisent
    opretion = input('Enter your opretion = ')
    
    if opretion == '1':
        name = input('Enter your name')
        if name in contacts :
            print(f'contact name {name} already exissts!')

        else:
           address = input('Enter your full address =')    
           email = input('Enter email =')
           mobil = input('Enter mobil number =')
           contacts[name]={'address':(address),'email':(email),'mobil':(mobil)}
           print(f'Contact name {name} has been created successfully!')
       
    elif opretion == '2':
        name = input('Enter contact name to view =')
        if name in contacts :
            contact = contacts[name]
            print(f'Name: {name}, address:{address}, email:{email}, mobil:{mobil}')
        else:
            print('contact not found!')

    elif opretion == '3':
        name = input('Enter name to update contact =')

        if name in contact:
            age = input('Enter update age =')
            email = input('Enter update email =')
            mobil = input('Enter update mobil number  =')
            contact[name]={'address':(address),'email':(email),'mobil':(mobil)}  
        else:
            print('contact not found!')

    elif opretion == '4':
        name = input('Enter contact name to delete =')
       
        if name in contact:
            del contacts[name]
            print(f'Contact name {name} has been delete successfully!')  

        else:
            print('Contact not found')

    elif opretion == '5':
        search_name = input('Enter contact name search =')
        Found = False

        for name , contact in contact.items():
            if search_name.lower() in name.lower():
                print(f'Found-name {name} , address:{address},mobil number:{mobil},email:{email},')      

                Found = True

            if not Found :
                print('No contact found with that name')
    
    elif opretion == '6':
        print(f'Total contacts found in your book:{len(contacts)}')
# this is the exit the program

    elif opretion == '7':
        print('Good bye......closing the program')
        break

    else:
        print('Invalid input')



