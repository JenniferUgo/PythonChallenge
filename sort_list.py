def sort_scattered_list(scattered_chars, word):
       
    sorted_chars = [] 
    for char in word:
        if char in scattered_chars:
            sorted_chars.append(char)
           
    return ''.join(sorted_chars)

scattered_list = ["h", "l", "m", "u", "b", "e"]
TARGET_WORD = "humble"
SORTED_WORD = sort_scattered_list(scattered_list, TARGET_WORD)
print(SORTED_WORD)




#     Question 1 

# Write a function that sorts a scattered list to become a word similar to the target word 
# For example 

# word = humble 
# list = ("h","l","m",“u",“b","e") 
# returns humble 

# return 
# -----
# String 