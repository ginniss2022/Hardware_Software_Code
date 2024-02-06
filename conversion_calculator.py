def binary_to_decimal():
    number = input("Enter a binary number:")
    result = 0
    if len(number) > 0:
        power = len(str(number)) - 1
        for num in str(number):
            result += int(num) * 2 ** power
            power -= 1
    print(f"Binary to Decimal: {result}")

def decimal_to_binary(number):
    result = ""
    number = int(number)
    while number > 0:
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result
    return result

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
    input('Hello, this is a conversion calculator \n ===> Press any key to continue <===')
    sel, choice = execute_display(menu_display())  
    print(sel, choice)
    operations = [binary_to_decimal, decimal_to_binary]
    running = True
    while running:
        operations[int(sel) - 1]


    # def main():
    #     num = input("Enter Binary Number:")
    #     print(f"Binary to Decimal: {binary_to_decimal(num)}")


# def main():
#     num = input("Enter Decimal Number:")  
#     print(f"Decimal {num} to Binary: {decimal_to_binary(num)}")

if __name__ == "__main__":
    main()