import time

def multiply(num1, num2):
  """
  This function multiplies two numbers without using the multiplication operator.

  Args:
      num1: The first number.
      num2: The second number (treated as the number of times to add num1).

  Returns:
      The product of num1 and num2.
  """

  product = 0
  start_time = time.time()  # Record overall start time

  # Time for function definition (mostly negligible)
  print(f"Function Definition Time: {time.time() - start_time:.5f} seconds")

  start_time_loop = time.time()  # Record start time for loop

  for i in range(abs(num2)):
    product += num1

  # Time for loop iterations
  print(f"Loop Iterations Time: {time.time() - start_time_loop:.5f} seconds")

  # Handle negative cases
  if num2 < 0:
    product = -product

  # Time for negative handling (usually negligible)
  print(f"Negative Handling Time: {time.time() - start_time_loop:.5f} seconds")  # This might not be accurate

  total_time = time.time() - start_time
  print(f"Overall Execution Time: {total_time:.5f} seconds")

  return product

# Example usage
num1 = 5
num2 = 3

# Multiply the numbers
result = multiply(num1, num2)

# Print the result
print("The product of", num1, "and", num2, "is:", result)
