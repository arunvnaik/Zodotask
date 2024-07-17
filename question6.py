def divide_numbers(numerator, divisor):
    try:
        result = numerator / divisor
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result

# Example usage:
num = 10
div = 0
print(divide_numbers(num, div))  

div = 2
print(divide_numbers(num, div)) 
