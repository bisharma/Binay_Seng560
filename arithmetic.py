
import math   # This will import math module

# Below are the basic arithematic functions created for
# performing basic arithematic calculations.

def add_num(num1, num2):
# Using arithmetic + Operator to add two numbers
    sum = float(num1) + float(num2)
    return sum

def sub_num(num1, num2):
# Using arithmetic - Operator to add two numbers
    subs = float(num1) - float(num2)
    return subs


def multiply_num(num1, num2):
# Using arithmetic * Operator to add two numbers
    mult = float(num1) * float(num2)
    return mult


def div_num(num1, num2):
# Using arithmetic / Operator to add two numbers
    div = float(num1) / float(num2)
    return div


def sqrt_num(num1):
# Using sqrt function from math lib to find the square root
    sqrt_output = math.sqrt(num1)
    return sqrt_output

def exp_num(num1, num2):
# Using arithmetic function * * to find the exponent
    exp_output = num1**num2
    return exp_output

# Now we will create basic conversion functions.

def float_to_hexa(float_num):
    result = float_num.hex()
    return result


def decimal_to_binary(decimal_num):
    result = bin(decimal_num)
    return result


def binary_to_decimal(binary_num):
    result = int(binary_num)
    return result


def decimal_to_octal(decimal_num):
    result = oct(decimal_num)
    return result

def octal_to_decimal(octal_num):
    result = int(octal_num)
    return result


def decimal_to_hexa(decimal_num):
    result = hex(decimal_num)
    return result

def hexa_to_decimal(hexa_num):
    result = int(hexa_num)
    return result
