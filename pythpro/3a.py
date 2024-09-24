from math import factorial

# Input values
n = int(input("Enter the number of terms (odd numbers only): "))
x = float(input("Enter the value of x: "))

# Initialize the sum and sign
summ = 0
sign = 1

# Loop through odd numbers (1, 3, 5, ..., up to n)
for i in range(1, 2*n, 2):  # Adjusting loop for n terms and odd powers
    term = sign * (x**i) / factorial(i)  # Compute each term
    summ += term  # Add term to the sum
    sign *= -1  # Alternate the sign

# Output the result
print(f"sin({x}) ≈ {summ}")
