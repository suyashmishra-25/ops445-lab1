def inches_to_cm(inches):

    return inches * 2.54



def cm_to_inches(cm):

    return cm / 2.54



def main():

    print("Converter Tool: Inches to Centimeters & Centimeters to Inches")

    

    while True:

        print("\n1. Convert inches -> cm")

        print("2. Convert cm -> inches")

        print("3. Exit")

        

        choice = input("Make your selection (1,2): ")



        if choice == "1":

            inches = int(input("Enter inches: "))

            print(f"Number of cm: {inches_to_cm(inches):.2f}")

        elif choice == "2":

            cm = int(input("Enter cm: "))

            print(f"Number of inches: {cm_to_inches(cm):.15f}")

        elif choice == "3":

            print("Invalid entry")

            break

        else:

            print("Invalid entry")



if __name__ == "__main__":

    main()


