#########################################################
# CS 1110A - Programming in Python                      #
# Module 3 - Exercise 6 - Unique characters in a string #
# Author: Ahmed Lotfey                                  #
# Date:   04/01/2023                                    #
#########################################################

def unique(s):
    """Prints unique characters in a string with only alphabetic uppercase and lowercase letters and whitespace
    all the lowercase letters come first followed by all the uppercase letters.
    """
    #  Create a list of unique characters
    unique_list = []
    #  Create a list of lowercase characters
    lower_list = []
    #  Create a list of uppercase characters
    upper_list = []
    #  Create a list of the merged lists
    merged_list = []

    #  Loop through the string
    for char in s:
        if char not in unique_list:
            unique_list.append(char)
    #  Loop through the unique list and add lowercase characters to lower_list
    for char in unique_list:
        if char.islower():
            lower_list.append(char)
    #  Loop through the unique list and add uppercase characters to upper_list
    for char in unique_list:
        if char.isupper():
            upper_list.append(char)
    # Sort the lowercase list
    lower_list.sort()
    # Sort the uppercase list
    upper_list.sort()
    #  merge the two lists
    merged_list = lower_list + upper_list
    # covert the list to a string
    merged_list_string = "".join(merged_list)
    #  Print the merged list
    print(f"Original string:   {merged_list_string}")


def main():
    # Print the program description
    print("Unique characters in a string\n")
    while True:
        # Ask user for a string
        ask_user = input("String: ")
        print()
        # Check if the user entered an empty string and break the loop if so and print "Done!"
        if len(ask_user) == 0:
            print("Done!")
            break
        # print the original string
        print(f"Original string:   {ask_user}")
        # call unique function
        unique(ask_user)
        print()


# run main function
if __name__ == "__main__":
    main()
