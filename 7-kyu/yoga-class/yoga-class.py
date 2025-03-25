def yoga(classroom, poses):
    count = 0
    for row in classroom:
        row_sum = sum(row)
        for p in row:
            for pose in poses:
                if row_sum + p >= pose:
                    count += 1
    return count