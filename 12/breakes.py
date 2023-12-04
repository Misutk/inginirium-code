def check_string_brackets(input_string: str):
    q = "("
    w = ")"
    t = 0
    i = 0
    for s in input_string:
        if q in s:
            i +=1
        if w in s:
            i-=1
    if i == 0:
        print("right")
    else:
        print("folst")

check_string_brackets("()()")