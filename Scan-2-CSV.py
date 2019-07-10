#!/usr/bin/env python

## Main ##            
if __name__ == "__main__":

    # Introduction and get a name for the file.
    print("\nWelcome to MU2 Barcode Scanning System")
    name = input("Enter name for file: ")
    name = name + ".csv"
    print("\nPlease type or scan into the fields below...\n")

    # Loop through all items.   *For the undo() command*
    while True:

        sn = mu = ""
        # Loop until you get a valid Serial Number.
        while True:
            sn = input("Serial Number:\n")
            print()
            # If Serial Number is Blank.
            if sn == "":
                sn = "NA"
            # If Serial Number is valid.
            if sn.isalnum() == True:
                break
            # If an invalid Serial Number
            else:
                print("ERROR: Invalid Serial Number")
                print("Please try again...")

        # Loop until you get a valid Inventory Number.
        while True:
            mu = input("MU2 Number:\n")
            print()
            # If number is empty.
            if mu == "":
                mu = "NA"
            # If number is valid.
            if mu.isalnum() == True:
                break
            # If number is invalid.
            else:
                print("ERROR: Invalid MU2 Number")
                print("Please try again...")

        # Allow a command or just continue to scan.
        cmd = input("Enter Command or Press Enter to Continue...\n")
        print()
        
        # If command undo() is called.
        if cmd == "undo()":
            print("Undoing last entries...")

        # If command stop() or quit() is called.
        elif cmd == "stop()" or cmd == "quit()":
            break

        # Else, append item to csv file.
        else:
            with open(name,"a+") as f:
                string = sn + "," + mu + "\n"
                f.write(string)

