
def function2():
    return 'Olá'

def function1(function2):
    return function2()

var = function1(function2)
print(var)