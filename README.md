# Binay_Seng560
Programming Assignment for SENG 560


SENG 560 – Software Reusability.

Test Cases:
(For test result, please scroll to the end of the document). 
How to use it:
1.	The library/package seng560_math contains following scripts.
a.	__init__.py
b.	arithmatic_wrapper_test.py
c.	arithmetic.py
d.	converter.py
e.	converter_withtests.py
2.	arithmetic.py holds the functions for doing basic mathematical operations such as :
a.	addition
b.	subtraction
c.	multiplication
d.	division
e.	square root
f.	exponent
3.	converter.py holds the functions for doing basic conversion. Conversion that can be made are as follows:
a.	binary to decimal
b.	decimal to binary
c.	decimal to octal
d.	octal to decimal
e.	decimal to hexadecimal
f.	hexadecimal to decimal.
4.	converter_withtests.py contains the wrapper script where user inputs the value and the respective conversion is made. This wrapper script invokes the converter.py script for calling the functions.
5.	arithmetic_wrapper_test.py is a wrapper script which when executed will ask the user to input what type of operation to be performed.
6.	Except square root, user is prompted to input two numerical values. 
7.	Then the script will return the calculated value.
8.	In order to use the library, __init__.py file has been created where all the functions are added importing from arithmetic.py and converter.py.
9.	All the scripts including __init__.py is included in the folder seng560_math.
10.	In order to use the library, the folder needs to be copied to the Python’s site-package folder. 
11.	In window, the general location would be something like this: H:\Binay Personal\Python\Lib\site-packages
12.	Once added, the wrapper scripts could be executed and values entered to test various scenarios. 

Exceptions:
1.	The screen shot from Python Shell after executing few test runs have been including in the word document. It can be found on the assignment submission page. 
2.	The initial scope of the work was to have the capability to perform calculations for binary, octal and hexadecimal numbers as well. The current script can add only integer and float. Author is a beginner Python programmer and thus will explore other features later.
3.	The initial concept was to convert binary, octal, hexadecimal to integer/float and invoke the arithematic functions and then covert back to respective binary, octal or hexadecimal values.  This has not been incorporated as a part of the scope of this work.  
4.	For test cases, authors have run the script and entered the values and got the intended results. Author has attached the screenshots. 
