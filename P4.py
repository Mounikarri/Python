# Get input from the user
input_string = input("Enter a string: ")

# Check the length and create the result
if len(input_string) < 2:
    result = ""
else:
    result = input_string[:2] + input_string[-2:]

# Display the result
print("Result:", result)
