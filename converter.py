
import math   # This will import math module

# Now we will create basic conversion functions.

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
