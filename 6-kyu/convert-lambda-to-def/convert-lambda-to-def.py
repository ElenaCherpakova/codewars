def convert_lambda_to_def(string):
    equal_index = string.find('=')
    name_fn = string[:equal_index].strip()
    lambda_index = string.find('lambda')
    colon_index = string.find(':', lambda_index)
    params = string[lambda_index + 7:colon_index].strip()
    body = string[colon_index + 1:].strip()
    return f'def {name_fn}({params}):\n    return {body}'
    