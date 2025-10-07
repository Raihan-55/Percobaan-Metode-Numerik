"# Percobaan-Metode-Numerik" 

Raihan Sahaja

21120123130093

This project implements four numerical methods to solve the system of nonlinear equations: x² + xy = 10 and y + 3xy² = 57. The implemented methods include Jacobi Fixed Point, Gauss-Seidel, Newton-Raphson, and Secant methods.

Among these methods, only Jacobi diverges due to its simultaneous iteration approach and sensitivity to initial guesses. The formulation x_new = (10 - x²) / y and y_new = √((57 - y) / (3 * x)) proves unstable as it cannot handle the strong coupling between equations effectively.

Gauss-Seidel improves upon Jacobi by using immediate updates, making it stable and practical for simple implementations. Newton-Raphson demonstrates the fastest convergence with quadratic speed, though it requires derivative calculations and more complex implementation. The Secant method offers a stable derivative-free alternative with good convergence properties.

For practical applications, Gauss-Seidel is recommended for quick implementations, Newton-Raphson for high accuracy and speed, and Secant for stability without derivatives. The project provides complete Python implementations with convergence analysis for each method, using initial guess (1.5, 3.5) and tolerance 1e-6.
