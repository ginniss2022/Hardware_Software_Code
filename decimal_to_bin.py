def decimal_to_binary(number):
    result = ""
    number = int(number)
    while number > 0:
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result
    return result

# const checkInt = (str) => {
#     const set = new Set([...1,2,3,4,5,6,7,8,9,0]);
#     for(let i = 0; i < str.length; i++){
#         if(!set.has(str[i])){
#            return false;
#         }
#     }
#     return true;
# }

def main():
    num = input("Enter Decimal Number:") 
    # checkInt(num)   
    print(f"Decimal {num} to Binary: {decimal_to_binary(num)}")

if __name__ == "__main__":
    main()