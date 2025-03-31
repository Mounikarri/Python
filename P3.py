import re

# Get input from the user
expression = input("Enter an algebraic expression: ")

# Add multiplication symbols
expression = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expression)  # Between digit and letter
expression = re.sub(r'([a-zA-Z])(\()', r'\1*\2', expression)  # Between letter and parenthesis
expression = re.sub(r'(\))([a-zA-Z\d])', r'\1*\2', expression)  # Between closing parenthesis and letter/digit

# Display the modified expression
print("Modified expression:", expression)

