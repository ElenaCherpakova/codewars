#preloaded variable: "dictionary"
​
def make_backronym(acronym):
    backron_dict = {
        'A': 'awesome', 'B': 'beautiful', 'C': 'confident', 'D': 'disturbing', 'E': 'eager', 
        'F': 'fantastic', 'G': 'gregarious', 'H': 'hippy', 'I': 'ingestable', 'J': 'joke', 
        'K': 'klingon', 'L': 'literal', 'M': 'mustache', 'N': 'newtonian', 'O': 'oscillating', 
        'P': 'perfect', 'Q': 'queen', 'R': 'rant', 'S': 'stylish', 'T': 'turn', 
        'U': 'underlying', 'V': 'volcano', 'W': 'weird', 'X': 'xylophone', 'Y': 'yogic', 
        'Z': 'zero'
    }
    return ' '.join(backron_dict[char.upper()] for char in acronym)