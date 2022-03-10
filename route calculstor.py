"""
This calculator takes values that could be written in a browsers route path as a single string. It then returns
the result as a number (or an error message).

Route paths use the '/' symbol so this can't be in our calculator. Instead we are using the '$' symbol as our
divide operator.

You will be passed a string of any length containing numbers and operators:

'+' = add
'-' = subtract
'*' = multiply
'$' = divide
Your task is to break the string down and calculate the expression using this order of operations.
(division => multiplication => subtraction => addition)

If you are given an invalid input (i.e. any character except .0123456789+-*$) you should return the error
message:'400: Bad request'

Remember:
Operations are infinite
Order of operations is imperitive
No eval or equivalent functions
Examples:

calculate('1+1')     => '2'
calculate('10$2')    => '5'
calculate('1.5*3')   => '4.5'

calculate('5+5+5+5') => '20'

calculate('1000$2.5$5+5-5+6$6') =>'81'

calculate('10-9p')   =>  '400: Bad request'
Further Notes - Parameters outside of this challenge:
Brackets e.g. 10*(1+2)
Square root, log, % or any other operators
Unary minus (10*-1)
Bad mathematical input (10**$10 or 5+5$)
You may have to deal with floats
If enjoy this and want something harder please see http://www.codewars.com/kata/evaluate-mathematical-expression/
for making a much more complicated calculator. This is a good kata leading up to that.
"""


def calculate(expression):
    operations = ("$", "*", "-", "+")
    exclusion_symbol = ("/", "<", ">", ",", ":", "^", "%", ")", "(", "#", "!", "?", "~")
    if set(expression).intersection(set(exclusion_symbol)):
        return "400: Bad request"

    for operation in operations:
        expression = expression.replace(operation, f" {operation} ")
    expression_in_list = expression.split(" ")

    for i in range(0,len(expression_in_list), 2):
        if not expression_in_list[i].isnumeric() and not "." in expression_in_list[i]:
            return "400: Bad request"

    if not set(operations).intersection(set(expression)):
        return float(expression)

    for operation in operations:
        while operation in expression_in_list:
            i = expression_in_list.index(operation)
            if expression_in_list[i] == "$":
                expression_in_list[i] = float(expression_in_list[i - 1]) / float(expression_in_list[i + 1])
                expression_in_list.pop(i + 1)
                expression_in_list.pop(i - 1)
            elif expression_in_list[i] == "*":
                expression_in_list[i] = float(expression_in_list[i - 1]) * float(expression_in_list[i + 1])
                expression_in_list.pop(i + 1)
                expression_in_list.pop(i - 1)
            elif expression_in_list[i] == "-":
                expression_in_list[i] = float(expression_in_list[i - 1]) - float(expression_in_list[i + 1])
                expression_in_list.pop(i + 1)
                expression_in_list.pop(i - 1)
            elif expression_in_list[i] == "+":
                expression_in_list[i] = float(expression_in_list[i - 1]) + float(expression_in_list[i + 1])
                expression_in_list.pop(i + 1)
                expression_in_list.pop(i - 1)

    return expression_in_list[0]


print(calculate("1000$2.5$5+5-5+6$6"))
print(calculate("10-9p"))
print(calculate("1.1"))
print(calculate("2/3.4,5"))
print(calculate("2/3<1/1"))
