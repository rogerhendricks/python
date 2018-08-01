def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3, 4, 5)

def print_kwargs(**kwargs):
    for kw in kwargs:
        print(kw, kwargs[kw])

print_kwargs(name="roger", month="August", drink="beer")

def print_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

print_args_kwargs(1, 2, 3, name="roger")

