# Name: Zaheer Safi
# Class: CS 341
# Date: 22 Feb 2024
# Project: This Project uses sqlite and python to execute quries on sqlite3 on the Database Chicago
# Lobbyist database by analyzing the number or lobbyist their compnsation and details about differnt lobbyists

import sqlite3
import objecttier

# Function to display general statistics about lobbyists, employers, and clients
def stats(dbConn):
    
    # Retrieve and print total counts using functions from objecttier module
    total_lobbyists = objecttier.num_lobbyists(dbConn)
    total_clients = objecttier.num_clients(dbConn)
    total_employers = objecttier.num_employers(dbConn)

    # Print formatted statistics
    print("General Statistics:")
    print(f"  Number of Lobbyists: {total_lobbyists:,}")
    print(f"  Number of Employers: {total_employers:,}")
    print(f"  Number of Clients: {total_clients:,}")

# Command 1: Search and display lobbyists based on name pattern
def command1(dbConn):
    
    print()
    # Input for lobbyist name or pattern
    Name_Pattern = input("Enter lobbyist name (first or last, wildcards _ and % supported): ")
    # Retrieve matching rows from database
    rows = objecttier.get_lobbyists(dbConn, Name_Pattern)
    
    # Display number of lobbyists found
    print()
   
    print(f"Number of lobbyists found: {len(rows)}")
    
    
    # Display details of each lobbyist if less than 101 lobbyists are found
    if len(rows) < 101:
        if rows:
            print()
            for row in rows:
                print(f"{row.Lobbyist_ID} : {row.First_Name} {row.Last_Name} Phone: {row.Phone}")
    else:
        # Message for too many results
        print()
        print("There are too many lobbyists to display, please narrow your search and try again...")

        
# Command 2: Display detailed information of a lobbyist based on ID
def command2(dbConn):
    print()
    # Input for lobbyist ID
    Lobbyist_ID = input("Enter Lobbyist ID: ")
    # Retrieve lobbyist details
    Details_obj = objecttier.get_lobbyist_details(dbConn, Lobbyist_ID)
    
    # Check if details exist and display them
    if Details_obj:
        print()
        # Display formatted details of the lobbyist
        print(Details_obj.Lobbyist_ID,":")
        print(f"  Full Name: {Details_obj.Salutation} {Details_obj.First_Name} {Details_obj.Middle_Initial} {Details_obj.Last_Name} {Details_obj.Suffix}")
        print(f"  Address: {Details_obj.Address_1} {Details_obj.Address_2} , {Details_obj.City} , {Details_obj.State_Initial} {Details_obj.Zip_Code} {Details_obj.Country}")
        print(f"  Email: {Details_obj.Email}")
        print(f"  Phone: {Details_obj.Phone}")
        print(f"  Fax: {Details_obj.Fax}")
        
        # Display years registered and employers in a comma-separated list
        print("  Years Registered: ", end = "")
        for i in Details_obj.Years_Registered:
            print(f"{i}, ", end = "")
        print()
        print("  Employers: ", end = "")
        for k in Details_obj.Employers:
            print(f"{k}, ", end = "")
        print()
        
        # Display total compensation
        print(f"  Total Compensation: ${Details_obj.Total_Compensation:,.2f}")
    else:
        # Message if no lobbyist is found with the given ID
        print()
        print("No lobbyist with that ID was found.")
    
# Command 3: Display top N lobbyists for a given year
def command3(dbConn):
    print()
    # Input for the number of lobbyists to display and the year
    Num = input("Enter the value of N: ")
    
    # Attempt to convert Num to an integer
    try:
        Num = int(Num)
        if Num <= 0:
            print("Please enter a positive value for N...")
            return
    except ValueError:
        print("Please enter a valid integer for N.")
        return

    Year = input("Enter the year: ")

    # Retrieve top N lobbyists for the given year
    rows = objecttier.get_top_N_lobbyists(dbConn, Num, Year)
    
    
    # Display details for each lobbyist
    if rows:
        print()
        i = 1
        for row in rows:
            print(i, ".", row.First_Name, row.Last_Name)
            print(" Phone:", row.Phone)
            print(f" Total Compensation: ${row.Total_Compensation:,.2f}")
            print("  Clients: ", end = "")
            for k in row.Clients:
                print(k, end = ", ")
            print()
            i += 1

# Command 4: Register a lobbyist for a given year
def command4(dbConn):
    
    print()
    # Input for year and lobbyist ID
    year = input("Enter year: ")
    ID = input("Enter the lobbyist ID: ")

    # Register the lobbyist for the given year
    func_return = objecttier.add_lobbyist_year(dbConn, ID, year)
    print()
    
    # Confirmation message based on the return value
    if func_return == 1:
        print("Lobbyist successfully registered.")
    else:
        print("No lobbyist with that ID was found.")

# Command 5: Set salutation for a lobbyist
def command5(dbConn):

    print()
    # Input for lobbyist ID and salutation
    ID = input("Enter the lobbyist ID: ")
    salutation = input("Enter the salutation: ")

    # Set the salutation for the lobbyist
    func_return = objecttier.set_salutation(dbConn, ID, salutation)
    print()
    if func_return == 1:
        print("Salutation successfully set.")
    else:
        print("No lobbyist with that ID was found.")

# Main function to execute the application
print('** Welcome to the Chicago Lobbyist Database Application **')
print()

# Establishing connection to the database
dbConn = sqlite3.connect('Chicago_Lobbyists.db')

# Display initial statistics
stats(dbConn)

print()
# Main loop for command input
cmd = input("Please enter a command (1-5, x to exit): ")
while cmd != "x":
    
    if   cmd == "1":
        command1(dbConn) 
    elif cmd == "2":
        command2(dbConn)
    elif cmd == "3":
        command3(dbConn)
    elif cmd == "4":
        command4(dbConn)
    elif cmd == "5":
        command5(dbConn)
    else:
        print("**Error, unknown command, try again...")
    print()

    cmd = input("Please enter a command (1-5, x to exit): ")


# Closing the database connection after exiting the loop
print()
dbConn.close()
