def main():
    # Prompt the user for two strings
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    # Check if the strings are of the same length
    if len(str1) != len(str2):
        print("The strings are not of the same length. Exiting the program.")
        return

    # Create a new string by alternating characters from the two strings
    result = ''.join(a + b for a, b in zip(str1, str2))

    # Print the resulting string
    print("Resulting string:", result)

if __name__ == "__main__":
    main()
