"""Read in a Fahrenheit temperature. 
Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F – 32)"""

def fahrenheit_to_calculus(fahrenheit):
    calculus = (5 / 9) * (fahrenheit - 32)
    return calculus

# Example usage:
temp_f = float(input("Enter temperature in Fahrenheit: "))
temp_c = fahrenheit_to_calculus(temp_f)
print(f"The equivalent calculus temperature is: {temp_c:.2f}")
