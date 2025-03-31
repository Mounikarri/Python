# Get input from the user
input_string = input("Enter a string: ")
suffix = input("Enter the suffix to check: ")

# Check if the string ends with the specified suffix
if input_string.endswith(suffix):
    print("The string ends with:", suffix)
else:
    print("The string does not end with:", suffix)


