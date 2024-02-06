
def binary_to_decimal(number):
    result = 0
    if len(number) > 0:
        power = len(str(number)) - 1
        for num in str(number):
            result += int(num) * 2 ** power
            power -= 1
        return result
    
def main():
    num = input("Enter Binary Number:")
    print(f"Binary to Decimal: {binary_to_decimal(num)}")

if __name__ == "__main__":
    main()   

    