def square(a):
    return a * a
    
def uniteString(string):
    return str(string) + str(string)
    

def callTwice(func = square, param = 5):
    param = func(param)
    param = func(param)
    
    return param
    
    
print(callTwice())

