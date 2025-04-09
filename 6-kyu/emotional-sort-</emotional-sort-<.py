def sort_emotions(arr, order):
    emotions = {':D': 1, ':)': 2, ':|': 3, ':(': 4, 'T_T': 5}
    sorted_arr = sorted(arr, key=lambda x: emotions[x], reverse=not order)
    return sorted_arr