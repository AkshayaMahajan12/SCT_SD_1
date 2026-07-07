def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


def display_menu(): 
    print("\n------------------------TEMPERATURE CONVERTER----------------------------")
    print("1. Celsius → Fahrenheit")
    print("2. Celsius → Kelvin")
    print("3. Fahrenheit → Celsius")
    print("4. Fahrenheit → Kelvin")
    print("5. Kelvin → Celsius")
    print("6. Kelvin → Fahrenheit")
    print("7. Convert Celsius to Both")
    print("8. Convert Fahrenheit to Both")
    print("9. Convert Kelvin to Both")
    print("0. Exit")
    print("-----------------------------------------")


while True:

    display_menu()

    try:
        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("\nThank you for using Temperature Converter!")
            break

        elif choice == 1:
            c = float(input("Enter Celsius: "))
            print(f"{c:.2f} °C = {celsius_to_fahrenheit(c):.2f} °F")

        elif choice == 2:
            c = float(input("Enter Celsius: "))
            print(f"{c:.2f} °C = {celsius_to_kelvin(c):.2f} K")

        elif choice == 3:
            f = float(input("Enter Fahrenheit: "))
            print(f"{f:.2f} °F = {fahrenheit_to_celsius(f):.2f} °C")

        elif choice == 4:
            f = float(input("Enter Fahrenheit: "))
            print(f"{f:.2f} °F = {fahrenheit_to_kelvin(f):.2f} K")

        elif choice == 5:
            k = float(input("Enter Kelvin: "))
            print(f"{k:.2f} K = {kelvin_to_celsius(k):.2f} °C")

        elif choice == 6:
            k = float(input("Enter Kelvin: "))
            print(f"{k:.2f} K = {kelvin_to_fahrenheit(k):.2f} °F")

        elif choice == 7:
            c = float(input("Enter Celsius: "))
            print("\nConversion Results")
            print("------------------")
            print(f"Fahrenheit : {celsius_to_fahrenheit(c):.2f} °F")
            print(f"Kelvin     : {celsius_to_kelvin(c):.2f} K")

        elif choice == 8:
            f = float(input("Enter Fahrenheit: "))
            print("\nConversion Results")
            print("------------------")
            print(f"Celsius : {fahrenheit_to_celsius(f):.2f} °C")
            print(f"Kelvin  : {fahrenheit_to_kelvin(f):.2f} K")

        elif choice == 9:
            k = float(input("Enter Kelvin: "))
            print("\nConversion Results")
            print("------------------")
            print(f"Celsius    : {kelvin_to_celsius(k):.2f} °C")
            print(f"Fahrenheit : {kelvin_to_fahrenheit(k):.2f} °F")

        else:
            print("Invalid choice! Please select between 0 and 9.")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")