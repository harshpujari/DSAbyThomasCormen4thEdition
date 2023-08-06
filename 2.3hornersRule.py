def horner_rule(coeffs, x):
    n = len(coeffs)
    result = coeffs[n - 1]

    for i in range(n - 2, -1, -1):
        result = result * x + coeffs[i]

    return result

if __name__ == "__main__":
    n = int(input("Enter the degree of the polynomial: ")) + 1
    coeffs = []
    for i in range(n):
        coeff = float(input(f"Enter coefficient a_{i}: "))
        coeffs.append(coeff)

    x = float(input("Enter the value of x: "))
    result = horner_rule(coeffs, x)
    print(f"The value of the polynomial at x={x} is:", result)
