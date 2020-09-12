def Add(num1, num2):
    num = num1 + num2
    print(num)
    return(num)


def Name(first, last):
    name = first + ' ' + last
    print(name)
    return(name)

def isDivisible(num, divider):
    result = num % divider
    print(result)
    return(result)
    

isDivisible(9, 3)