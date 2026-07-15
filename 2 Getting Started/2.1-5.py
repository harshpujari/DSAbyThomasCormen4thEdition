def add_binary_integers(A, B, n):
    """Add two n-bit binary integers A and B and return an (n+1)-bit result C."""
    C = [0] * (n + 1)
    carry = 0

    for i in range(n - 1, -1, -1):
        total = A[i] + B[i] + carry
        C[i + 1] = total % 2
        carry = total // 2

    C[0] = carry
    return C


if __name__ == "__main__":
    # Example: A = 1011 (11), B = 1101 (13), n = 4
    A = [1, 0, 1, 1]
    B = [1, 1, 0, 1]
    n = 4
    C = add_binary_integers(A, B, n)
    print("A:", A)
    print("B:", B)
    print("C:", C)
    print("Binary sum:", ''.join(str(bit) for bit in C))
