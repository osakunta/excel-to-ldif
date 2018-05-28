
def clean(value):
    value = str(value).lower()
    value = value.replace('\n', '').replace('.0', '').replace(' ', '')
    return value
