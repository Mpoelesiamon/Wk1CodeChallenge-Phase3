def solve(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    values = {char: ord(char) - 96 for char in consonants}
    
    substrings = ['']
    for char in word:
        if char in consonants:
            substrings[-1] += char
        else:
            substrings.append('')
    
    max_value = 0
    for substring in substrings:
        value = sum(values[char] for char in substring)
        max_value = max(max_value, value)
    
    print(f"The highest value of consonant substrings is: {max_value}")
    return max_value

# Example usage
solve("zodiacs")
