def sort_words_alphabetically(input_string):
    words = input_string.split()  
    sorted_words = sorted(words)
    sorted_string = ""
    for word in sorted_words:
        sorted_string += word + " "
    
    return sorted_string

input_string = "mohammad rami yousef ahmad basel"
sorted_string = sort_words_alphabetically(input_string)

print("Sorted string:", sorted_string)
