# https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature#Celsius_(centigrade)
# https://en.wikipedia.org/wiki/Celsius
# https://en.wikipedia.org/wiki/Kelvin
# https://en.wikipedia.org/wiki/Fahrenheit

def celsius_to_kelvin(xs):
    l=[]
    for x in xs:
        l.append(x+273.15)      
    return l

def celsius_to_kelvin(xs):
    return list(map(lambda x:x+273.15,xs))


def kelvin_to_celsius(xs):
    l=[]
    for x in xs:
        l.append(x-273.15)  
    return l

def kelvin_to_celsius(xs):
    return list(map(lambda x:x-273.15,xs))


def celsius_to_fahrenheit(xs):
    l=[]
    for x in xs:
        l.append(x*1.8+32)      
    return l

def celsius_to_fahrenheit(xs):
    return list(map(lambda x:x*1.8+32,xs))


def fahrenheit_to_celsius(xs):
    l=[]
    for x in xs:
        l.append((x-32)/1.8)      
    return l

def fahrenheit_to_celsius(xs):
    return list(map(lambda x:(x-32)/1.8,xs))


celsius_to_kelvin([0, 1, 2]) == [273.15, 274.15, 275.15]
kelvin_to_celsius([0, 1, 2]) == [-273.15, -272.15, -271.15]
celsius_to_fahrenheit([0, 5, 10]) == [32, 41, 50]
fahrenheit_to_celsius([32, 41, 50]) == [0, 5, 10]
