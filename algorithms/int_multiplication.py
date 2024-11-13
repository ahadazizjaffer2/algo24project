# # def visualize_integer_multiplication(file_path):
# #     steps = []

# #     def karatsuba(x, y):
# #         steps.append(f'<b>Multiplying {x} and {y}</b>')
        
# #         if x < 10 or y < 10:
# #             steps.append(f'<b>Returning product {x * y}</b>')
# #             return x * y

# #         n = max(len(str(x)), len(str(y)))
# #         half = n // 2
        
# #         high1, low1 = divmod(x, 10 ** half)
# #         high2, low2 = divmod(y, 10 ** half)
        
# #         z0 = karatsuba(low1, low2)
# #         z1 = karatsuba((low1 + high1), (low2 + high2))
# #         z2 = karatsuba(high1, high2)
        
# #         result = (z2 * 10 ** (2 * half)) + ((z1 - z2 - z0) * 10 ** half) + z0
# #         steps.append(f'<b>Karatsuba result of {x} and {y} = {result}</b>')
# #         return result

# #     with open(file_path, 'r') as f:
# #         # Clean the input by removing commas or any unwanted characters
# #         line = f.readline().replace(',', '').strip()
# #         x, y = map(int, line.split())  # Split and convert to integers
    
# #     result = karatsuba(x, y)
# #     result_str = f'<u>The product of {x} and {y} is {result}</u>'
    
# #     return steps, result_str


# def visualize_integer_multiplication(file_path):
#     steps = []

#     def karatsuba(x, y, steps_count):
#         indent = ' ' * (steps_count * 15)

#         steps.append(f'{indent}Multiplying {x} and {y}')
        
#         if x < 10 or y < 10:
#             steps.append(f'{indent}Returning product {x * y}')
#             return x * y

#         n = max(len(str(x)), len(str(y)))
#         half = n // 2
        
#         high1, low1 = divmod(x, 10 ** half)
#         high2, low2 = divmod(y, 10 ** half)
        
#         z0 = karatsuba(low1, low2, steps_count + 1)
#         z1 = karatsuba((low1 + high1), (low2 + high2), steps_count + 1)
#         z2 = karatsuba(high1, high2, steps_count + 1)
        
#         result = (z2 * 10 ** (2 * half)) + ((z1 - z2 - z0) * 10 ** half) + z0
#         steps.append(f'{indent}Karatsuba result of {x} and {y} = {result}')
#         steps_count += 1
#         return result

#     with open(file_path, 'r') as f:
#         line = f.readline().replace(',', '').strip()
#         x, y = map(int, line.split())  
    
#     steps.append(f'The integers to multiply are {x} and {y}')
#     result = karatsuba(x, y, 0)
#     result_str = f'The product of {x} and {y} is {result}'  
    
#     return steps, result_str


def visualize_integer_multiplication(file_path):
    steps = []

    def karatsuba(x, y, steps_count):
        indent = ' ' * (steps_count * 15)
        
        steps.append(f'{indent}Multiplying {x} and {y}')

        # Base case for recursion
        if x < 10 or y < 10:
            steps.append(f'{indent}Returning product {x * y}')
            return x * y

        # Calculate the size of the numbers
        n = max(len(str(x)), len(str(y)))
        half = n // 2
        steps.append(f'{indent}Splitting numbers at half-length {half} digits')

        # Split x and y into high and low parts
        high1, low1 = divmod(x, 10 ** half)
        high2, low2 = divmod(y, 10 ** half)
        
        steps.append(f'{indent}  High and low parts of {x}: high1 = {high1}, low1 = {low1}')
        steps.append(f'{indent}  High and low parts of {y}: high2 = {high2}, low2 = {low2}')

        # Recursive steps
        steps.append(f'{indent}Calculating z0 as the product of {low1} and {low2}')
        z0 = karatsuba(low1, low2, steps_count + 1)

        steps.append(f'{indent}Calculating z1 as the product of ({low1} + {high1}) and ({low2} + {high2})')
        z1 = karatsuba((low1 + high1), (low2 + high2), steps_count + 1)

        steps.append(f'{indent}Calculating z2 as the product of {high1} and {high2}')
        z2 = karatsuba(high1, high2, steps_count + 1)

        # Combine the results
        steps.append(f'{indent}Combining results:')
        steps.append(f'{indent}  - z2 * 10^({2 * half}) = {z2 * 10 ** (2 * half)}')
        steps.append(f'{indent}  - (z1 - z2 - z0) * 10^{half} = {(z1 - z2 - z0) * 10 ** half}')
        steps.append(f'{indent}  - z0 = {z0}')

        result = (z2 * 10 ** (2 * half)) + ((z1 - z2 - z0) * 10 ** half) + z0
        steps.append(f'{indent}Karatsuba result of {x} and {y} = {result}')

        return result

    with open(file_path, 'r') as f:
        # Clean the input by removing commas or any unwanted characters
        line = f.readline().replace(',', '').strip()
        x, y = map(int, line.split())  # Split and convert to integers

    steps.append(f'Starting Karatsuba multiplication for integers {x} and {y}')
    result = karatsuba(x, y, 0)
    result_str = f'The product of {x} and {y} is {result}'  
    
    return steps, result_str
