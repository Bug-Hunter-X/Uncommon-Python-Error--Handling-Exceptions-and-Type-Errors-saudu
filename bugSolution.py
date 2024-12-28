def improved_function(a, b):
    try:
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("Inputs must be numbers")
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

# Example demonstrating the improved solution
result1 = improved_function(10, 2) #works fine
print(f"Result 1: {result1}")

result2 = improved_function(10, 0) #catches ZeroDivisionError
print(f"Result 2: {result2}")

result3 = improved_function("10", 2) #catches TypeError
print(f"Result 3: {result3}")

result4 = improved_function(10, "2") #catches TypeError
print(f"Result 4: {result4}")

result5 = improved_function([10], 2) #catches TypeError
print(f"Result 5: {result5}")
