


#task 1,2,3

def make_bold(func):
    def wrapper(*args, **kwargs):
        return "<strong>" + func(*args, **kwargs) + "</strong>"
    return wrapper

def make_italics(func):
    def wrapper(*args, **kwargs):
        return "<em>" + func(*args, **kwargs) + "</em>"
    return wrapper

def make_paragraph(func):
    def wrapper(*args, **kwargs):
        return "<p>" + func(*args, **kwargs) + "</p>"
    return wrapper

@make_bold
def get_full_name(first, last):
    return f"{first} {last}"

@make_paragraph
@make_italics
def get_custom_html_greeting(first, last):
    full_name = get_full_name(first, last)
    return f"Hello, {full_name}!"

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))

#-----------------------------------------------------------------

def wrap_with(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"<{tag}>" + func(*args, **kwargs) + f"</{tag}>"
        return wrapper
    return decorator

@wrap_with(tag="strong")
def get_full_name(first, last):
    return f"{first} {last}"

@wrap_with(tag="p")
@wrap_with(tag="em")
def get_custom_html_greeting(first, last):
    full_name = get_full_name(first, last)
    return f"Hello, {full_name}!"

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))

