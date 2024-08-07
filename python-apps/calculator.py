
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

number_1 = float(input("Enter number 1: "))
number_2 = float(input("Enter number 2: "))

operator = input("Enter operator: ")

if operator == "+":
    print(number_1 + number_2)

elif operator == "-":
    print(number_1 - number_2)

elif operator == "*":
    print(number_1 * number_2)

elif operator == "/":
    print(number_1 / number_2)

use_converter = input("Would you like convert celsius to farenheit?: ")



if use_converter == "yes":
    celcius = float(input("Celcius: "))
    celsius_to_faranheit = celcius * 9 / 5 + 32


    print(celsius_to_faranheit, "degrees farenheit")

else:
    print("Goodbye")
