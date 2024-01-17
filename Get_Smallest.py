def Get_Smallest(smallest, value):
    value = int(value)
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    return smallest

def main():
    smallest = None
    while True:
        num = input("Enter a number: ").lower()
        if num == "done":
            break
        smallest = Get_Smallest(smallest, num)
        print("Smallest number is:", smallest)

main()