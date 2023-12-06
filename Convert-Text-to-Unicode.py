# Function to convert user input into its Unicode representation in \uXXXX format
def convert_to_unicode():
    # Prompting the user for input
    user_input = input("Enter the text to convert to Unicode: ")

    # Converting the input into Unicode representation in \uXXXX format
    unicode_representation = ''.join(f'\\u{ord(char):04X}' for char in user_input)

    # Returning the Unicode representation
    return unicode_representation

# Example usage
unicode_result = convert_to_unicode()
print("Unicode Representation:", unicode_result)
