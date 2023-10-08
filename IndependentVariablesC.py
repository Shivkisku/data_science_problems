import sympy as sp

# Define symbols
c = sp.symbols('c')
Var_X = sp.symbols('Var_X')
Var_Y = sp.symbols('Var_Y')
Cov_XY = sp.symbols('Cov_XY')

# Define the covariance expression
covariance_AB = c * Var_X + (1 + c) * (-0.2) * sp.sqrt(Var_X * Var_Y) + c * (-0.2) * sp.sqrt(Var_X * Var_Y) + (1 + c) * Var_Y

# Solve for c when Cov(A, B) = 0
solutions = sp.solve(covariance_AB, c)

# Display the solutions
print("Values of c for which A and B are independent:")
for solution in solutions:
    print(solution)
