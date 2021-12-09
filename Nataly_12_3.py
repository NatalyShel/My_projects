##########################################################################
#Author: Nataly
#Date: 09.12.2021
#Task: Read contacts from csv file. For that create classes:
# PhoneContact and Phone, define funcitons to load contacts from 
# csv file and organize search of contacts by phrase.
##########################################################################

# import PhoneContacts from Packages
import Packages.PhoneContacts as PC

# create object of class Phone
phone = PC.Phone()

# load contacts from file
phone.load_contacts_from_csv('contacts.csv')

# ask user to enter phrase to search contacts
phrase = input("Enter phrase to earch contacts -> ")

# call search funciton
phone.search_contacts(phrase)