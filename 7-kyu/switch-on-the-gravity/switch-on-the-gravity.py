def switch_gravity(lst):
    height = len(lst)
    width = len(lst[0])
    result = [['-' for _ in range(width)] for _ in range(height)]
    
    for col in range(width):
        count = 0
        for row in range(height):
            if lst[row][col] == "#":
                count += 1
        for row in range(height):
            if row >= height - count:
                result[row][col] = "#"
            else:
                result[row][col] = "-"
    return result