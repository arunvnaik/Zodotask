def arithmetic_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operator."

# Example usage:
print(arithmetic_operation(10, 5, '+'))  
print(arithmetic_operation(10, 5, '-'))  
print(arithmetic_operation(10, 5, '*'))  
print(arithmetic_operation(10, 5, '/'))  
print(arithmetic_operation(10, 0, '/'))  
print(arithmetic_operation(10, 5, '^'))  
