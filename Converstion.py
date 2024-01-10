def main():
    print("Welcome to my conversation program")
    conversation()
    print("Thanks for chatting with me")


def conversation():
    print("Do you like coding in python? Answer yes or no")
    answer = input().lower()
    if answer == "yes":
        print("That's good - the United States needs more coders!!")
    else: 
        print("Perhaps you will change your mind")
    print("Goodbye")

main()