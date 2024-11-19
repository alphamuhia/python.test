# finding newton method

def newton_root(func, deriv, initial_guess, tolerance=1e-7, max_iterations=1000):
    x = initial_guess
    for _ in range(max_iterations):
        f_x = func(x)
        df_x = deriv(x)
        if abs(f_x) < tolerance:
            return x
        if df_x == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x -= f_x / df_x
    raise ValueError("Exceeded maximum iterations.")


root = newton_root(lambda x: x**2 - 2, lambda x: 2*x, initial_guess=1)
print(root) 

# fibonacci sequence

def fibonacci(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

print(fibonacci(10))  

# gcd

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))  
