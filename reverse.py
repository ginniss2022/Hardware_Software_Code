def intro_msg():
    return input("Enter a string to reverse it:")

def reverse_word(characters):
    reverse_string=""
    i = 0
    while i < len(characters):
        reverse_string = characters[i] + reverse_string
        i += 1
    print(f"Your string in reverse: {reverse_string}")


def main():
    run = True
    while run:
        word = intro_msg()
        word = reverse_word(word)
        if input('Press "q" to exit or hit enter to continue') == 'q' or "Q":
            exit()
main()
