def to_jaden_case(string):
    words = string.split(' ')
    return ' '.join(word.capitalize() for word in words)
        
            