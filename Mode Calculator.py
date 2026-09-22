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