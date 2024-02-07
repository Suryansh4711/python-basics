#contacatination
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

#Repetition
repeated_text = "Repeat" * 3
print(repeated_text)

#Length
text = "Python"
length = len(text)
print("Length:", length)

# Remove leading and trailing whitespace
trimmed_text = text.strip()
print(trimmed_text)

#convert to lowercase and uppercase
lower_case = text.lower()
upper_case = text.upper()
print("Lowercase:", lower_case)
print("Uppercase:", upper_case)

#true/false(isalpha/isdigit)
text = "abc"
print(text.isalpha())  #Output: True

text = "abc123"
print(text.isalpha())  #Output: False

text = "123"
print(text.isdigit())  #Output: True

text = "123bcs"
print(text.isdigit())  #Output: False