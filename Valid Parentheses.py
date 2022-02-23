"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore,
the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as
parentheses (e.g. [], {}, <>).
"""


def valid_parentheses(string):
    open = "("
    close = ")"
    stack = []
    is_good = True
    n_string = ''
    for s in string:
        if s in (open, close):
            n_string += s
    for s in n_string:
        if s == open:
            stack.append(s)
        elif s == close:
            if not stack:
                is_good = False
                break
            open_brecked = stack.pop()
            if open_brecked == open and s == close:
                continue
            is_good = False
            break
    if is_good and len(stack) == 0:
        return True
    else:
        return False


print(valid_parentheses("(())((()())())"))
print(valid_parentheses('hi(hi)()'))
print(valid_parentheses('  ('))
