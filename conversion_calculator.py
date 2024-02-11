def binary_to_decimal():
    number = input("Enter a binary number:")
    for char in str(number):
        if char != "0" and char != "1":
            print("Not a valid binary number")
            return 

    result = 0
    if len(number) > 0:
        power = len(str(number)) - 1
        for num in str(number):
            result += int(num) * 2 ** power
            power -= 1
    print(f"Binary {number} to Decimal: {result}")

def decimal_to_binary():
    number = input("Enter Decimal Number:")  
    result = ""
    try:
        number = int(number)
    except ValueError:
        print("Not a valid integer")
        return
    while number > 0:
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result
    print(f"Decimal {number} to Binary: {result}")

def execute_display(menu_dict):
    for items, values in menu_dict.items():
        print(f"{items}. {values.capitalize()}")
        menu_selection = list(menu_dict.keys())
        selection = "#"
    
    while selection not in menu_selection:
        selection = input("Enter: ")
        if selection not in menu_selection:
            print("Invalid entry!")

    return selection, menu_dict[selection]

def menu_display():
    menu_dict = {
        "1": "decimal_to_binary",
        "2":"binary_to_decimal",
        "3":"exit_program"
    }
    return menu_dict

def main():
    input('Hello, this is a conversion calculator \n ===> Press enter to continue <===')
    sel, choice = execute_display(menu_display())   
    operations = [ decimal_to_binary, binary_to_decimal, exit ]
    running = True
    while running:
        operations[int(sel) - 1]()
        s = input("Type 'q' to quit or hit enter to continue: ")
        if s.lower() == "q":
            break
    print("Thanks for using my conversion calculator, have a great day.")

if __name__ == "__main__":
    main()