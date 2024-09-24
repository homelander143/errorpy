from math import factorial

# Input from user
n = int(input("Enter the number of terms: "))
x = float(input("Enter the value of x: "))

# Initialize the sum (cos(0) = 1) and sign (alternates between -1 and +1)
summ = 1
sign = -1

# Loop through even powers: 2, 4, 6, ..., up to 2n
for i in range(2, 2*n, 2):
    summ += ((x**i) * sign) / factorial(i)  # Add each term to the sum
    sign *= -1  # Alternate the sign for next term

# Output the result
print(f"cos({x}) ≈ {summ}")
