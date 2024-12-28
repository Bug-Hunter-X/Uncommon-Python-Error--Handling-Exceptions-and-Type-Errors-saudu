def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid input type")
        return None

# Example demonstrating the bug
result1 = function_with_uncommon_error(10, 2) #works fine
print(f"Result 1: {result1}")

result2 = function_with_uncommon_error(10, 0) #catches ZeroDivisionError
print(f"Result 2: {result2}")

result3 = function_with_uncommon_error("10", 2) #catches TypeError
print(f"Result 3: {result3}")

result4 = function_with_uncommon_error(10, "2") #another TypeError
print(f"Result 4: {result4}")

result5 = function_with_uncommon_error([10], 2) #another TypeError
print(f"Result 5: {result5}")
