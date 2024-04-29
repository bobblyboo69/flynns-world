import pandas as pd 

def menu_options():
     print("-WELCOME TO HOTEL FLYNN-")
     print("\n1. check room details\n2. create booking\n3. view booking\n4. add room details")
     c = int(input("select which you would like to choose"))

     if c == 1:
        room_details()
     elif c == 2:
         create_booking()
     elif c == 3:
         view_booking()
     elif c == 4:
        add_roomdetails()


    
        



def room_details():


def create_booking():
    name = input("enter name")
    number = int(input("enter the vaccant room number"))
    print ("select a privellige\n1.master class\n2. peasant class")
    privellige = input()
    if privellige == "1":
        privellige = "master"
    elif privellige == "2":
        privellige = "peasant"
    else:
        print("enter a number 1-3 pls")
        create_booking()
    s


    

def view_booking():

def add_roomdetails():

     