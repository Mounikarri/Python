def convert_to_uppercase(s):
    # Count uppercase letters in the first four characters
    uppercase_count = sum(1 for char in s[:4] if char.isupper())
    # If there are at least two uppercase letters, return the uppercase version of the string
    if uppercase_count >= 2:
        return s.upper()
    return s

# Example usage
input_string = input("Enter a string: ")
print("Result:", convert_to_uppercase(input_string))

