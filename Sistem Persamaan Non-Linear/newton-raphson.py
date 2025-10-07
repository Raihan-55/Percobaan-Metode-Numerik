import math

def newton_raphson_g1A_g2B(x0, y0, epsilon=0.000001, max_iter=100):
    def f1(x, y):
        return x - (10 - x**2) / y

    def f2(x, y):
        if (57 - y) / (3 * x) < 0:
            raise ValueError("Domain negatif pada akar sqrt di f2.")
        return y - math.sqrt((57 - y) / (3 * x))

    def df1_dx(x, y):
        return 1 + (2 * x) / y

    def df1_dy(x, y):
        return -(10 - x**2) / (y**2)

    def df2_dx(x, y):
        h = 1e-6
        return (f2(x + h, y) - f2(x - h, y)) / (2 * h)

    def df2_dy(x, y):
        h = 1e-6
        return (f2(x, y + h) - f2(x, y - h)) / (2 * h)

    print(f"{'r':<3} {'x':<12} {'y':<12} {'deltaX':<12} {'deltaY':<12}")
    x, y = x0, y0
    print(f"{0:<3} {x:<12.6f} {y:<12.6f} {0.000000:<12.6f} {0.000000:<12.6f}")

    for r in range(1, max_iter + 1):
        try:
            F1 = f1(x, y)
            F2 = f2(x, y)

            J11 = df1_dx(x, y)
            J12 = df1_dy(x, y)
            J21 = df2_dx(x, y)
            J22 = df2_dy(x, y)

            detJ = J11 * J22 - J12 * J21
            if abs(detJ) < 1e-12:
                print("Error: Determinan Jacobian mendekati nol.")
                break

            delta_x = (-F1 * J22 + F2 * J12) / detJ
            delta_y = (-J11 * F2 + J21 * F1) / detJ

            x_new = x + delta_x
            y_new = y + delta_y

            print(f"{r:<3} {x_new:<12.6f} {y_new:<12.6f} {abs(delta_x):<12.6f} {abs(delta_y):<12.6f}")

            if abs(delta_x) < epsilon and abs(delta_y) < epsilon:
                print("Konvergen.")
                print(f"Hasil akhir: x = {x_new:.6f}, y = {y_new:.6f}")
                return x_new, y_new

            x, y = x_new, y_new

        except ValueError as e:
            print(f"Iterasi ke-{r}: {e}")
            break

    print("Tidak konvergen dalam max_iter.")
    return x, y

# Jalankan
newton_raphson_g1A_g2B(1.5, 3.5)
