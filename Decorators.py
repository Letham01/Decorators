


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

#to be cont.