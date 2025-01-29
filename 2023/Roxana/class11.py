

def remove_space(s):
    x = ""
    for ch in s:
        if ch != ' ':
             x = x + ch
    return x





print(remove_space("This is a sentence."))
