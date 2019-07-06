
def sanitize(data):
    if data is None:
        data = ''
    return str(data).strip().replace('"\\n"', '\n')
