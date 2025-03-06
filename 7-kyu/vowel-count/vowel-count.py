def get_count(sentence):
    vowels = 'aeiou'
    return 0 if not sentence else sum(1 for char in sentence if char in vowels)
​