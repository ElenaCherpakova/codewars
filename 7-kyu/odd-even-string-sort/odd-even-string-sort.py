def sort_my_string(s):
    # even, odd = '', ''
    # for i, letter in enumerate(s):
    #     if i % 2 == 0:
    #         even +=letter
    #     else:
    #         odd += letter
    # return f'{even} {odd}'
    return f"{s[::2]} {s[1::2]}"
