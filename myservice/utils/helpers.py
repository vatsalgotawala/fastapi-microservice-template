# function to convert a snake case string into a camel case
def camelcase(input_string):
    parts = iter(input_string.split("_"))
    return next(parts) + "".join(i.title() for i in parts)
