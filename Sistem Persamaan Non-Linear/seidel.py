import math

def seidel_fixed_point(x0, y0, epsilon=1e-6, max_iter=100):
    print(f"{'r':<3} {'x':<12} {'y':<12} {'deltaX':<12} {'deltaY':<12}")
    x = x0
    y = y0
    print(f"{0:<3} {x:<12.6f} {y:<12.6f} {0.000000:<12.6f} {0.000000:<12.6f}")

    for r in range(1, max_iter + 1):
        try:
            # Iterasi Seidel: x baru langsung digunakan untuk menghitung y
            x_new = (10 - x**2) / y
            if 3 * x_new == 0 or (57 - y) / (3 * x_new) < 0:
                print("Terjadi kesalahan (akar negatif atau pembagi nol). Iterasi berhenti.")
                break
            y_new = math.sqrt((57 - y) / (3 * x_new))
        except ValueError:
            print("Error: Domain negatif pada sqrt.")
            break

        delta_x = abs(x_new - x)
        delta_y = abs(y_new - y)

        print(f"{r:<3} {x_new:<12.6f} {y_new:<12.6f} {delta_x:<12.6f} {delta_y:<12.6f}")

        if delta_x < epsilon and delta_y < epsilon:
            print("Konvergen.")
            print(f"Hasil akhir: x = {x_new:.6f}, y = {y_new:.6f}")
            return x_new, y_new

        x = x_new
        y = y_new

    print("Tidak konvergen dalam max_iter.")
    return x, y

# Jalankan
seidel_fixed_point(1.5, 3.5)
