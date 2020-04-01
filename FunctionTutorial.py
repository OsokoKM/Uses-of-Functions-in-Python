#Functions that print and don't give you information
def printHi():
    print("Hi")
    
printHi()


#functions with parameters
def printThis(param):
    print(param)
    
printThis("Subscribe?")


#functions which give back information when you give some to it. These are the most common ones
def square(num):
    return num*num
    
num1 = square(5)
print(num1)


#functions which don't take but give information
string = "Smash that like and sub butttoon!!!"
def giveLength():
    return len(string)
    
print(giveLength())


#functions which call other functions

def callXTimes(amount, func, val):

    for i in range(amount):
        val = func(val)
        
    return val
    
print(callXTimes(5, square, 2))

#set default param

def uniteString(string):
    return str(string) + str(string)
    
def callTwice(func = square, param = 2):
    param = func(param)
    param = func(param)
    return param
    
a = callTwice(uniteString, "Consider Subscribing?")

print(a)