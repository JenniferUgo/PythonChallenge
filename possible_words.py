def generate_words(scrambled_chars, word_list):
    def is_word_possible(word, letters):
        word_count = {}
        for char in letters:
            word_count[char] = word_count.get(char, 0) + 1
        for char in word:
            if char not in word_count or word_count[char] == 0:
                return False
            word_count[char] -= 1
        return True

    possible_words = []
    for word in word_list:
        if is_word_possible(word, scrambled_chars):
            possible_words.append(word)
    return possible_words

list_of_words = ["apple", "fruits", "mango", "heal"]
scrambled_list = ["a", "p", "1", "r", "u", "i", "t", "s", "h", "e", "n", "g", "o", "f"]
poss_words = generate_words(scrambled_list, list_of_words)
print(poss_words) 





# Question 2
# Write a function that generates as many words from a scrambled list given a list of words 

# e.g 
# list_of_words = ["apple", "fruits", "mango", "heal"} 
# scrambled_list = ["a","p","1","r","u","i","t","s","h","e","n","g*,"o", "f"]
                  
# return
# -----
# List 
