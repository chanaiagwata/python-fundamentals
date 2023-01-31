#!/usr/bin/env python3.10

from contact import Contact

def create_contact(fname,lname,phone,email):
    '''
    Function that create a new contact
    '''
    new_contact = Contact(fname,lname,phone,email)
    return new_contact

def save_contacts(contact):
    '''
    Function to save contact
    '''
    contact.save_contact()

def del_contact(contact):
    '''
    Function to delete contact
    '''
    contact.delete_contact()

def find_contact(number):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Contact.find_by_number(number)

def check_existing_contact(number):
    '''
    Function that check if a contact exists with that number and return a boolean
    '''
    return Contact.contact_exist(number)

def display_contacts():
    '''
    Function that returns all the saved contacts
    '''
    return Contact.display_contacts()

def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use short codes : cc - create a new contact, dc - display contacts, fc - find a contact, ex - exit the contact list ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Contact")
            print("-"*10)

            print("First name...")
            f_name = input()

            print("Last name...")
            l_name = input()

            print("Phone number...")
            p_number = input()

            print("Email address...")
            e_address = input()

            save_contacts(create_contact(f_name,l_name,p_number,e_address)) #create and save new contact

            print('\n')
            print(f"New Contact {f_name} {l_name} created")
            print ('\n')
        elif short_code == 'dc':
            
    