

def validate_numeric(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                return "The input arguments must be numeric"
        for arg in kwargs.values():
            if not isinstance(arg, (int, float)):
                return "The input arguments must be numeric"
        return func(*args, **kwargs)
    return wrapper

@validate_numeric
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b

print(sum(1, 2))
print(sum(1, "2"))
print(sum(a=1, b="a"))
print(sum(a=1, b=3.4))
#---------------------------

def debug(func):
    def wrapper(*args, **kwargs):
        positional_args = ", ".join(map(str, args))
        keyword_args = ", ".join(f"{key}={value}" for key, value in kwargs.items())

        print("****************")
        if positional_args:
            print(f"Positional arguments: {positional_args}")
        else:
            print("No positional arguments")
        if keyword_args:
            print(f"Keyword arguments: {keyword_args}")
        else:
            print("No keyword arguments")

        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper

@debug
def sum(a, b, **kwargs):
    return a + b

sum(1, 2)
sum(a=1, b=2)
sum(a=1, b=2, c=3)

#---------------------------




