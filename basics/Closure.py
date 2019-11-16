text = "global text"


def outer_func():
    text = "enclosing text"

    def inner_func():
        nonlocal text
        text = 'nonlocal test not next level anymore!'
        print('inner_func:', text)  # inner_func: inner text

    print('outer_func:', text)  # outer_func: enclosing text
    inner_func()
    print('outer_func:', text)  # outer_func: enclosing text

outer_func()
print('global:', text)  # global: global text