def word_in_word(word_a, word_b):
    
    ''' Take two words as input
        Check if the first word can be made from the letters of the second
    '''
    # Counts frequency of each possible letter
    letters = set(word_a + word_b)
    available_letters = {}
    for b in letters:
        available_letters.update({b : word_b.count(b)})
    
    # Checks that each letter needed appears at most the maximum possible number of times
    valid = True
    for a in set(word_a):
        if not(available_letters[a] >= word_a.count(a)):
            valid = False
            break
        
    if not valid:
        return f"The word {word_a} cannot be formed from the word {word_b}"
    else:
        return f"The word {word_a} can be formed from the word {word_b}"
    
    
    
def mode_calculator(n_input):
    
    ''' Returns the frequency of the mode for a set of digits
        Unless multiple digits have the maximum frequency
    '''
    
    # Gets required number of digits
    nums = []
    for i in range(n_input):
        nums.append(int(input()))
    
    # Calculates mode
    max_val = 0
    multi = False
    for n in set(nums):
        if nums.count(n) > max_val:
            max_val = nums.count(n)
            multi = False
        elif nums.count(n) == max_val:
            multi = True
    return (max_val if not multi else "Data was multimodal")

print(mode_calculator(3))
