user_input = 'random'
lst = []

def menu():
    print('''\nMenu
    1. Add an item
    2. Mark as done
    3. View the items in the list
    4. Exit
    ''')
while user_input != '4':

    menu()
    user_input = input("Enter your Choice: ")

    if user_input == "1":
        item = input("Enter todo item:- ")
        lst.append(item)
        print('Item added\n')

    elif user_input == '2':
        item = input('Enter item to be marked/deleted done: ')
        if item in lst:
            lst.remove(item)
        else:
            print('Item not in the list.')
        print('Marked Item: ', item)

    elif user_input == '3':
        print('\nTodo List')
        for item in lst:
            print(f">> {item}")

    elif user_input == '4':
        print('Goodbye!!')
        
    else:
        print('Please enter 1, 2, 3 or 4 as choice.')