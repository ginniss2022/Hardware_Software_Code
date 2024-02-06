def decimal_to_binary(number):
    result = ""
    number = int(number)
    while number > 0:
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result
    return result

def main():
    num = input("Enter Decimal Number:")  
    print(f"Decimal {num} to Binary: {decimal_to_binary(num)}")

if __name__ == "__main__":
    main()