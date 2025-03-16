def initials(name):
    words = name.split()
    initials = ''
    for word in words[:-1]:
        initials += word[0].upper() + '.'
    last_name = words[-1].capitalize()
    return f'{initials}{last_name}'