
import seng560_math   # This will import math module


## Author: Binay Sharma
## 09/15/2017

## NOTE :The below script performs basic conversion from
## decimal to octal
## octal to decimal
## decimal to hexa
## hexa to decimal
## decimal to binary
## binary to decimal

## The script converter.py has the function defined for each conversion

## Note: As a part of this work, the function is not robust to handle float/fraction.
## Author will revisit the scope in the future. 


## The below logic invokes function decimal_to_hexa for test.
dec = input("Enter the decimal number (50) to convert to hexa:")

dec_to_hexa = seng560_math.decimal_to_hexa(dec)
print ("decimal 50  to hexa:",dec_to_hexa)
 

## The below logic invokes function hexa_to_decimal for test.
hexa = input("Enter the hex (0x32) number to convert to dec:")

hexa_to_decimal_test = seng560_math.hexa_to_decimal(hexa)
print (" hexa 0x32 to decimal:", hexa_to_decimal_test)


## The below logic invokes function decimal_to_octal for test.

dec_for_octa = input("Enter the decimal number (50) to convert to octal:")

decimal_to_octal_test = seng560_math.decimal_to_octal(dec_for_octa)
print ("decimal 50 to octa:", decimal_to_octal_test)


## The below logic invokes function octal_to_decimal for test.
octal = input("Enter the octal number (0o62) to convert to decimal:")

octal_to_decimal_test = seng560_math.octal_to_decimal(octal)
print ("octal 0o62 to decimal:", octal_to_decimal_test)


## The below logic invokes function decimal_to_binary for test.
dec_for_binary = input("Enter the decimal number (19) to convert to binary:")

decimal_to_binary_test = seng560_math.decimal_to_binary(dec_for_binary)
print (" decimal 19 to binary :", decimal_to_binary_test)


## The below logic invokes function binary_to_decimal for test.
binary = input("Enter the binary number (0b10011) to convert to decimal:")

binary_to_decimal_test = seng560_math.binary_to_decimal(0b10011)
print ("binary 0b10011 to decimal:", binary_to_decimal_test)


