def horner_rule(coeffs, x):
    n = len(coeffs)
    result = coeffs[n - 1]

    for i in range(n - 2, -1, -1):
        result = result * x + coeffs[i]

    return result

# Example usage:
if __name__ == "__main__":
    coeffs = [3, -6, 5, -2]  # Polynomial coefficients: 3x^3 - 6x^2 + 5x - 2
    x = 2
    result = horner_rule(coeffs, x)
    print(f"The value of the polynomial at x={x} is:", result)
