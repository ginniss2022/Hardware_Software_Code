def check_int_number(number):
    try:
        return (False, int(number))
    except:
        print("Invalid input!!")
        return (True, None)
    
def main():
    make_selection = True
    while make_selection:
        selection = input("Select a whole number from:")
        make_selection, selection = check_int_number(selection)
    print("Good job", selection, "is a whole number!!")

main()