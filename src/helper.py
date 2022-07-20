from pyrsistent import s

FALSE_STRING = {"n", "no", "none", "null", "", "false", "f", None, False}


def string_to_bool(string: str) -> bool:
    string = string.strip().lower()
    return False if string in FALSE_STRING else True
