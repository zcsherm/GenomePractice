import string
import random
import math

def generate_id(length=10):
    """
    Generate a 'unique' id for an object
    :param length: the length of the id
    :return: the id as a string
    """
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return ''.join(random.choices(characters, k=length))
"""
Add more functions or trim? Maybe give each one 2 bytecodes, but some only have 1?
"""

func_names = ['linear', 'inverse linear', 'exponential', 'inverse exponential', 'radical', 'inverse radical', 'sigmoid', 'inverse sigmoid', 'negative square root']

def linear():
    def linear_func(x):
        return x
    return linear_func

def inverse_linear():
    def inv(x):
        return 1-x
    return inv
    
def exponential(exponent):
    """
    Exponent in range of 1-16?
    """
    def exp(x):
        return x ** exponent
    return exp

def inverse_exponential(exponent):
    def inv_exp(x):
        return 1 - x ** exponent
    return inv_exp
    
def radical(radicand):
    """
    Radicand in range of 1-16
    """
    def rad(x):
        return x**(1/radicand)
    return rad

def inverse_radical(radicand):
    def rad(x):
        return 1 - x**(1/radicand)
    return rad

def sigmoid(coefficient, mean):
    """
    Coefficient is 1 to 128
    Mean is 0-1 maybe 1/(1 to 128) to avoid IEEE754
    """
    def sig(x):
        return 1 / (1 + math.e ** ((coefficient * x * -1) + (1/mean * coefficient)))
    return sig

def reverse_sigmoid(coefficient, mean):
    func = sigmoid(coefficient, mean)
    def sig(x):
        return (-1*func(x) + 1)
    return sig

def reverse_square(base, coefficient):
    """
    sqrt(base ^ (-tx))
    base = 1-65 -> 1+ base/16
    coefficient = 1-65
    """
    def rev(x):
        return (base ** (coefficient * x * -1)) ** .5
    return rev

def health_decay(health, param):
    """
    Essentially functions like a halflife for organ health
    (1-(currenthealth-param_val) * currenthealth ???
    """
