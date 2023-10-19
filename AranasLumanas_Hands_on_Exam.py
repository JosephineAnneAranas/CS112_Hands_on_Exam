print("----------------------------------")
option = eval(input("(1) Decimal number to Binary number \n" "(2) Decimal number to Octal number \n""(3) Decimal number to Hexadecimal number\n" "Enter a number to get the following conversion: " ))
print("----------------------------------")
if option == 1:
    decimal_binary = int(input("Enter a decimal value to convert: "))
    binary_to_decimal = format(decimal_binary, "b")
    print(f"The binary value of {decimal_binary} is {binary_to_decimal}.")

elif option == 2:
    decimal_octal = int(input("Enter a decimal value to convert: "))
    octal_to_decimal = format(decimal_octal, "o")
    print(f"The octal value of {decimal_octal} is {octal_to_decimal}.")

elif option == 3:
    decimal_hexadecimal = int(input("Enter a decimal value to convert: "))
    hexadecimal_to_decimal = format(decimal_hexadecimal, "x")
    print(f"The hexadecimal value of {decimal_hexadecimal} is {hexadecimal_to_decimal}.")

else: print("Invalid Option. Enter options from 1-3 only")
print("----------------------------------")
