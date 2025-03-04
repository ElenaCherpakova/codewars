def create_box(m, n):  ## m and n positive integers
    matrix = []
    for i in range(n):
        row = []
        for j in range(m): 
            top = i
            bottom = n-1-i
            left = j
            right = m-1-j
            min_distance_to_any_edge = min(top, bottom, left, right) + 1
            row.append(min_distance_to_any_edge)
        matrix.append(row)
    return matrix