#######################################
# CS 1110A - Programming in Python    #
# Module 3 - Exercise 5 - Palindromes #
# Author: Ahmed Lotfey                #
# Date:   04/01/2023                  #
#######################################


def is_palindrome(s):
    """Check if it is plaindrome or not."""
    # Reverse the string.
    plaindrome = s[::-1]
    # Check if the string is a palindrome.
    if plaindrome == s:
        print("This string is a palindrome.\n")
    else:
        print("This string is not a palindrome.\n")


# call the function with the user input.
def main():
    # This program checks if a string is a palindrome or not.
    print("Is a string a palindrome?\n")
    while True:

        user_input = input("Enter a string: ")
        if len(user_input) == 0:
            print("\nDone!\n")
            break
        is_palindrome(user_input)

# call the main function.
if __name__ == "__main__":
    main()
