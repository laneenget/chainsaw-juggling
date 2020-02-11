import sqlite3

def main():
    conn = sqlite3.connect('chainsaw_db.sqlite') #Create/open db file
    display_menu()
    while True:
        command = input('Command: ')
        command = command.lower
        if command == 'create':
            create_row()
        elif command == 'read':
            read_row()
        elif command == 'update':
            update_row()
        elif command == 'destroy':
            delete_row()
        elif command == 'exit':
            quit()
            break
        else:
            print('That is not a valid command. Please try again.')

def display_menu():
    print('CRUD')
    print('create -- Create a record holder')
    print('read -- Read a record holder')
    print('update -- Update a record holder')
    print('destroy -- Delete a record holder')
    print('exit -- Exit program')
    print('')

def table_init():
    conn.execute('create table records (name text, country text, catches integer)') #Add table

#def create_row():

def read_row():
    name = input('Enter name of the record holder: ')
    row = conn.execute('select from records values (?)', (name))
    print(row)

#def update_row():

#def delete_row():

def quit():
    print('Bye!')

main()