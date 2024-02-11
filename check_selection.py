def check_selection(numbers):
    hex_list = ["A","B","C","D","E","F","0", "1", "2", "3", "4","5","6","7","8","9"]

    for number in numbers:
        if number.upper() in hex_list:
            return True
    print("Not a dexadecimal number")
    return False

def main():
    good_selection = True
    while good_selection:
        selection = input("Provide a hexadecimal number:")
        good_selection = check_selection(selection)
    print("Good Job", selection, "is a hexadeimal number!!!")

main()

# 3.	Is it possible to modify the code to only use good_selection and remove selection? Is this a good idea?	
# Yes it is possible, but at that point you might as well put it all into the main function. 