import math

print("Nama: Raihan Sahaja")
print("NIM : 21120123130093")
print("-" * 60)

def jacobi_fixed_point(x0, y0, epsilon=0.000001, max_iter=100):
    print(f"{'r':<3} {'x':<12} {'y':<12} {'deltaX':<12} {'deltaY':<12}")
    x = x0
    y = y0
    print(f"{0:<3} {x:<12.6f} {y:<12.6f} {0.000000:<12.6f} {0.000000:<12.6f}")
    
    for r in range(1, max_iter + 1):
        try:
            x_new = (10 - x**2) / y  # g1A
            y_new = math.sqrt((57 - y) / (3 * x))  # g2B
        except ValueError:
            print("Error: Domain negatif pada sqrt.")
            break
        
        delta_x = abs(x_new - x)
        delta_y = abs(y_new - y)
        
        print(f"{r:<3} {x_new:<12.6f} {y_new:<12.6f} {delta_x:<12.6f} {delta_y:<12.6f}")
        
        if delta_x < epsilon and delta_y < epsilon:
            print("Konvergen.")
            return x_new, y_new
        x = x_new
        y = y_new
    
    print("Tidak konvergen dalam max_iter.")
    return x, y

# Jalankan
jacobi_fixed_point(1.5, 3.5)

def secant_method_simple(x0, y0, x1, y1, epsilon=0.000001, max_iter=100):
    def f1(x, y):
        return x**2 + x * y - 10

    def f2(x, y):
        return y + 3 * x * y**2 - 57

    print(f"{'r':<3} {'x':<12} {'y':<12} {'deltaX':<12} {'deltaY':<12}")
    print(f"{0:<3} {x0:<12.6f} {y0:<12.6f} {'-':<12} {'-':<12}")
    print(f"{1:<3} {x1:<12.6f} {y1:<12.6f} {abs(x1-x0):<12.6f} {abs(y1-y0):<12.6f}")

    for r in range(2, max_iter + 1):
        # Delta untuk setiap variabel menggunakan Secant univariat
        delta_x = -f1(x1, y1) * (x1 - x0) / (f1(x1, y1) - f1(x0, y0)) if f1(x1, y1) != f1(x0, y0) else 0
        delta_y = -f2(x1, y1) * (y1 - y0) / (f2(x1, y1) - f2(x0, y0)) if f2(x1, y1) != f2(x0, y0) else 0

        x2 = x1 + delta_x
        y2 = y1 + delta_y

        print(f"{r:<3} {x2:<12.6f} {y2:<12.6f} {abs(delta_x):<12.6f} {abs(delta_y):<12.6f}")

        if abs(delta_x) < epsilon and abs(delta_y) < epsilon:
            print("Konvergen.")
            print(f"Hasil akhir: x = {x2:.6f}, y = {y2:.6f}")
            return x2, y2

        x0, y0 = x1, y1
        x1, y1 = x2, y2

    print("Tidak konvergen dalam max_iter.")
    return x1, y1

# Jalankan
secant_method_simple(1.5, 3.5, 1.6, 3.4)
