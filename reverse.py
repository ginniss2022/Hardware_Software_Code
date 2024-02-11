def intro_msg():
    print("I can reverse a string")
    print("If you give me 'apple' i will return 'elppa'")
    print("I can even do an entire sentence")
    return input("Type something and see:")

def reverse_word(characters):
    reverse_string=""
    i = 0
    while i < len(characters):
        reverse_string = characters[i] + reverse_string
        i += 1
    print(f"Below is your string in reverse: \n{reverse_string}")


def main():
    word = intro_msg()
    word = reverse_word(word)

main()
