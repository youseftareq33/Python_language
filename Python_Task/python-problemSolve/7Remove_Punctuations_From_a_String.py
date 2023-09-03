import string

def remove_punctuation(input_string):
    cleaned_string = ""
    for char in input_string:
        if char not in string.punctuation:
            cleaned_string += char
            
    return cleaned_string


input_string = "Hello, how are u?"
cleaned_string = remove_punctuation(input_string)

print("Cleaned string:", cleaned_string)
