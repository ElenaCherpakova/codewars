def check_logs(log):
    if len(log) == 1:
        return 1
    if not log:
        return 0
    days = 1
    for i in range(1, len(log)):
        current_time = log[i]
        prev_time = log[i-1]
        if current_time <= prev_time:
            days +=1
    return days
                   