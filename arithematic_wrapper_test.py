# Created By: Binay Sharma
# Date: 2017/09/16
# SENG 560 - SOFTWARE REUSE

# The purpose of this wrapper script is to test to perform basic
# arithmetic operations such as:
#   Addition
#   Subtraction
#   Multiplication
#   Division
#   Square Root
#   Exponent

# Please note that author mostly works on DI tools which less indulges into programming.
# Author has learnt Python recenty, hence there might be some discrepencies/erros, which
# author believes would be ignored.

import seng560_math

# First we will ask User to define which type of operation they would like to perform

oper = input("Enter what type of operation you would like to perform? : ")

# Following are the expected values

#   Addition - add
#   Subtraction - subs
#   Multiplication - multiply
#   Division - divide
#   Square Root - squareroot
#   Exponent - exponent

try:
    if oper =='add':
        print('we will perform addition here')
        try:
            num1 = input( "Enter the first number to be added:")
            num2 = input( "Enter the second number to be added:")
            print(num1)
            print(num2)                       
            result = seng560_math.add_num(num1,num2)
            print (result)
        except:
            print("Please check the correct number of values.")            
    elif str(oper) == 'subs':
        print('we will perform subtraction here')
        try:
            num1 = input( "Enter the first number to perfrom subtraction:")
            num2 = input( "Enter the second number to perform subtraction:")
            print(num1)
            print(num2)  
            result = seng560_math.sub_num(num1,num2)
            print (result)
        except:
            print("Please check the correct number of values.")    
    elif str(oper) == 'multiply':
        print('we will perform multiplication here')
        try:
            num1 = input( "Enter the first number to perfrom multiplication:")
            num2 = input( "Enter the second number to perform multiplication:")       
            print(num1)
            print(num2)  
            result = seng560_math.multiply_num(num1,num2)
            print (result)
        except:
            print("Please check the correct number of values.")            
    elif str(oper) == 'divide':
        print('we will perform division here')
        try:
            num1 = input( "Enter the first number to perfrom division:")
            num2 = input( "Enter the second number to perform division:") 
            print(num1)
            print(num2)  
            result = seng560_math.div_num(num1,num2)
            print (result)
        except:
            print("Please check the correct number of values.")         
    elif str(oper) == 'squareroot':
        print('we will find square root here')
        try:
            num1 = input( "Enter a number for finding the square root:")     
            print(num1)
            result = seng560_math.sqrt_num(float(num1))
            print (result)
        except:
            print("Please enter the single number for finding the square root.")      
    elif str(oper) == 'exponent':
        print('we will find exponent here')
        try:
            num1 = input( "Enter the first number (base) to perfrom exponent:")
            num2 = input( "Enter the second number (power) to perform exponent:")
            print(num1)
            print(num2)  
            result = seng560_math.exp_num(float(num1), float(num2))
            print (result)
        except:
            print("Please check the correct number of values.")        
    else:
        print(' There is no operation to be performed.')
except:
    print("Please pass the correct number of input variables here.")
print('************* operation is complete ***********************')
