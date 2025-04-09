def sort_emotions(arr, order):
    emotions = {':D':5, ':)': 4, ':|': 3, ':(': 2,'T_T': 1}
    return sorted(arr, key=lambda x: emotions[x], reverse=order)