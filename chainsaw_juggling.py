import sqlite3

def main():
    conn = sqlite3.connect('chainsaw_db.sqlite') #Create/open db file

def display_menu():
    print('CRUD')
    print('create -- ')
    print('read -- ')
    print('update -- ')
    print('destroy -- ')

def table_init():
    conn.execute('create table records (name text, country text, catches integer)') #Add table

def add_row():

def update_row():

def delete_row():

def quit():
