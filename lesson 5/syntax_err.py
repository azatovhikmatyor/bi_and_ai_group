# SyntaxError

# try:
#     a = {'a': 10
#     a["b"]
# except SyntaxError:
#     print("Syntax error occured")

try:
    a = "print('Hello World'"
    eval(a)
except SyntaxError:
    print('Syntax error occured')