def main():
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

if __name__ == "__main__":
    main()