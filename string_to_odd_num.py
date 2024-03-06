def string_to_odd_number(input_string):
    output_result = ""
    for char in input_string:
        if char.isdigit():
            digit = int(char)
            if digit % 2 != 0:
                output_result += char
    return int(output_result)

string_input = "4157"
result = string_to_odd_number(string_input)
print(result)








# Question 3 

# Write a function that converts a string to numbers removing any even digit from that number. Each letter is
# represented from 1-26(a-z)
# example 
# dog = 4157 = 157