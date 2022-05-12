def zero(f=None):
    return 0 if not f else round_value(name_function=f, value=0)


def one(f=None):
    return 1 if not f else round_value(name_function=f, value=1)


def two(f=None):
    return 2 if not f else round_value(name_function=f, value=2)


def three(f=None):
    return 3 if not f else round_value(name_function=f, value=3)


def four(f=None):
    return 4 if not f else round_value(name_function=f, value=4)


def five(f=None):
    return 5 if not f else round_value(name_function=f, value=5)


def six(f=None):
    return 6 if not f else round_value(name_function=f, value=6)


def seven(f=None):
    return 7 if not f else round_value(name_function=f, value=7)


def eight(f=None):
    return 8 if not f else round_value(name_function=f, value=8)


def nine(f=None):
    return 9 if not f else round_value(name_function=f, value=9)


def round_value(name_function, value):
    return round(name_function(value))


def plus(value):
    return lambda x: x + value


def minus(value):
    return lambda x: x - value


def times(value):
    return lambda x: x * value


def divided_by(value):
    return lambda x: x / value
