import sqlite3

def main():
    conn = sqlite3.connect('chainsaw_db.sqlite') #Create/open db file
    conn.execute('create table if not exists records (firstname text, lastname text, country text, catches integer)') #Add table
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
    first_name, last_name, country, catches = input('Enter first name, last name, country, and catches of the new record holder separated by spaces. ').split()
    conn.execute('insert into records values (?, ?, ?, ?)', (first_name, last_name, country, catches))
    conn.commit()

def read_row(conn):
    first_name, last_name = input('Enter full name of the record holder: ').split() #Take user input
    cur = conn.execute('select * from records WHERE firstname = ? AND lastname = ?', (first_name, last_name)) #Query db using input
    row = cur.fetchone()
    print(row) #Print result

def update_row(conn):
    firstname, lastname = input('Enter full name of the record holder: ').split()
    catches = int(input('Enter the updated number of catches: '))
    conn.execute('UPDATE records SET catches = ? WHERE firstname = ? AND lastname = ?', (catches, firstname, lastname))
    conn.commit()

def delete_row(conn):
    firstname, lastname = input('Enter full name of the record holder: ').split()
    conn.execute('delete from records where firstname = ? and lastname = ?', (firstname, lastname))
    conn.commit()

main()