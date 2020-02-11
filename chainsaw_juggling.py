import sqlite3

def main():
    conn = sqlite3.connect('chainsaw_db.sqlite') #Create/open db file
    conn.execute('create table if not exists records (name text, country text, catches integer)') #Add table
    display_menu() #Call display function
    while True:
        command = input('Command: ') #Take user input
        command = command.lower() #Validate input
        if command == 'create':
            create_row(conn) #Call create
        elif command == 'read':
            read_row(conn) #Call read
        elif command == 'update':
            update_row(conn) #Call update
        elif command == 'destroy':
            delete_row(conn) #Call delete
        elif command == 'exit':
            print('Bye!') #Quit program
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

def create_row(conn):
    name, country, catches = input('Enter name, country, and catches of the new record holder separated by commas. ')
    conn.execute('insert into records values (?, ?, ?)', (name, country, catches))
    conn.commit

def read_row(conn):
    name = input('Enter name of the record holder: ') #Take user input
    row = conn.execute('select from records values (?)', (name)) #Query db using input
    print(row) #Print result

#def update_row():

#def delete_row():

main()