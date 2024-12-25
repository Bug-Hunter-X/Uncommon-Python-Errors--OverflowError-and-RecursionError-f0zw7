def function_with_uncommon_error(a, b):
    try:
        if abs(a) > 10**300 or abs(b) > 10**300:
            print("Error: Input numbers are too large")
            return None
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Invalid input type. Please provide numbers only.")
        return None
    except OverflowError:
        print("Error: The result of the operation is too large.")
        return None

# Solution for RecursionError: Add a check to prevent exceeding a certain recursion depth.

def recursive_function(n, max_depth=1000):
    if n == 0:
        return 0
    elif n > max_depth:
      print("Error: Recursion depth exceeded.")
      return None
    else:
        return recursive_function(n - 1, max_depth) + 1

# Example usage (should not raise OverflowError or RecursionError)
large_number = 10**10
result = function_with_uncommon_error(large_number, 2)
print(result)
print(recursive_function(500))