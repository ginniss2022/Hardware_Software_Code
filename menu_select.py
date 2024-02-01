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
    sel, choice = execute_display(menu_display())
    print(f"You selected {sel} and want to convert {choice}")

if __name__ == "__main__":
    main()   